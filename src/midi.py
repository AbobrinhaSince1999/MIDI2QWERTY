from .constants import OFFSET_MAP
from .qwerty import QWERTY

def offset_note(note, offset):
    i = max(0, min(offset, 6))
    # Normalize note by subtracting offset
    value = OFFSET_MAP[i]
    
    if note >= value:
        return note - value
    
    return -1  # Invalid if below offset range

def msg_handle(msg, config):
    # Ignore timing and sensing messages
    if msg.type not in ["clock", "active_sensing"]:
        
        # Handle sustain pedal
        if msg.type == "control_change" and msg.control == 64:
            if msg.value >= 64:
                if config["sustain"]["toggle-mode"]: 
                    QWERTY.press(config["sustain"]["key"])
                else: 
                    QWERTY.hold(config["sustain"]["key"])
            else:
                if config["sustain"]["toggle-mode"]:
                    QWERTY.press(config["sustain"]["key"])
                else: 
                    QWERTY.release(config["sustain"]["key"])

        # Handle note on messages
        if msg.type == "note_on" and msg.velocity > 0:
            # Normalize and send note to QWERTY
            normalized = offset_note(msg.note, config["offset"])
            QWERTY.play(normalized)
