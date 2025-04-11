from textual.app import App, ComposeResult
from textual.widgets import Button, Tab, Tabs, Header, Input, Label, Switch
from textual.containers import Container, Vertical
import yaml
import threading
import mido
from pathlib import Path
from src.midi import msg_handle

CONFIG_PATH = Path("./config.yaml")

class MyApp(App):
    CSS = """
    Header {
        dock: top;
        width: 100%;
        height: 3;
        color: white;
        text-style: bold;
        padding: 0 2;
        background: $primary;
        margin-bottom: 1;
    }

    #content {
        padding: 2;
    }

    .hidden {
        display: none;
    }

    .visible {
        display: block;
    }

    #midi-content {
        align: center middle;
    }

    Button {
        margin: 1;
        width: 22;
        text-style: none;
    }

    Input {
        width: 25;
        margin: 1;
    }

    Switch {
        margin: 1;
    }

    Label {
        padding-left: 2;
    }
    """

    def __init__(self):
        super().__init__()
        self.config_data = {}
        self.midi_thread = None
        self.midi_running = False
        self.stop_event = threading.Event()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Tabs(
            Tab("MIDI", id="midi-tab"),
            Tab("Config", id="config-tab"),
        )

        yield Container(
            # MIDI Tab
            Vertical(
                Button("Connect to MIDI", id="midi-switch", variant="success"),
                Label("🔌 Disconnected", id="midi-status"),
                id="midi-content",
                classes="visible"
            ),

            # Config Tab
            Vertical(
                Vertical(Label("Sustain Key:"), Input(id="sustain-key")),
                Vertical(Label("Sustain Toggle Mode:"), Switch(id="toggle-mode")),
                Vertical(Label("Offset (0–6):"), Input(id="offset-input")),
                Button("Save Config", id="save-config", variant="primary"),
                id="config-content",
                classes="hidden"
            ),

            id="content"
        )

    def on_mount(self):
        self.title = "MIDI2QWERTY 🎹"
        self.load_config()

    def load_config(self):
        try:
            with open(CONFIG_PATH, "r") as f:
                self.config_data = yaml.safe_load(f)
        except FileNotFoundError:
            self.config_data = {
                "sustain": {"key": "space", "toggle-mode": True},
                "offset": 0
            }

        self.query_one("#sustain-key", Input).value = self.config_data["sustain"]["key"]
        self.query_one("#toggle-mode", Switch).value = self.config_data["sustain"]["toggle-mode"]
        self.query_one("#offset-input", Input).value = str(self.config_data.get("offset", 0))

    def save_config(self):
        self.config_data["sustain"]["key"] = self.query_one("#sustain-key", Input).value
        self.config_data["sustain"]["toggle-mode"] = self.query_one("#toggle-mode", Switch).value

        try:
            self.config_data["offset"] = max(0, min(6, int(self.query_one("#offset-input", Input).value)))
        except ValueError:
            self.config_data["offset"] = 0

        with open(CONFIG_PATH, "w") as f:
            yaml.dump(self.config_data, f)

    def start_midi(self) -> bool:
        def midi_loop():
            try:
                input_ports = mido.get_input_names()
                if not input_ports:
                    self.log("⚠️ No MIDI devices found.")
                    return

                with mido.open_input(input_ports[0]) as port:
                    self.log(f"🎧 Listening on {input_ports[0]}")
                    for msg in port:
                        if self.stop_event.is_set():
                            break
                        msg_handle(msg, self.config_data)
            except Exception as e:
                self.log(f"⚠️ MIDI error: {e}")

        input_ports = mido.get_input_names()
        if not input_ports:
            return False

        self.stop_event.clear()
        self.midi_thread = threading.Thread(target=midi_loop, daemon=True)
        self.midi_thread.start()
        self.midi_running = True
        return True

    def stop_midi(self):
        self.stop_event.set()
        self.midi_thread = None
        self.midi_running = False

        self.query_one("#midi-status", Label).update("🔌 Disconnected")
        self.query_one("#midi-switch", Button).label = "Connect to MIDI"

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        midi = self.query_one("#midi-content")
        config = self.query_one("#config-content")
        midi.set_class(event.tab.id == "midi-tab", "visible")
        midi.set_class(event.tab.id != "midi-tab", "hidden")
        config.set_class(event.tab.id == "config-tab", "visible")
        config.set_class(event.tab.id != "config-tab", "hidden")

    async def on_button_pressed(self, event: Button.Pressed):
        match event.button.id:
            case "midi-switch":
                if self.midi_running:
                    self.stop_midi()
                else:
                    if self.start_midi():
                        self.query_one("#midi-status", Label).update("🎵 Connected")
                        self.query_one("#midi-switch", Button).label = "Disconnect MIDI"
                    else:
                        self.query_one("#midi-status", Label).update("⚠️ No device found")
            case "save-config":
                self.save_config()

if __name__ == "__main__":
    app = MyApp()
    app.run()
