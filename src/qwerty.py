import keyboard as kb
from .constants import KEY_MAP

class QWERTY:
    @staticmethod
    def play(index: int):
        # Play mapped key if index is within range
        if 0 <= index < len(KEY_MAP):
            KEY_MAP[index]()
        else:
            print(f"Note (index {index}) is out of mapped range.")

    @staticmethod
    def hold(key: str):
        # Hold down a key
        kb.press(key)

    @staticmethod
    def release(key: str):
        # Release a held key
        kb.release(key)

    @staticmethod
    def press(key: str):
        # Press and release a key
        kb.press_and_release(key)
