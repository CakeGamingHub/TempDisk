import platform
import os
import sys

import Tkinter

def checkOS():
	if platform.system().upper() != "LINUX":
		statusLabel.config(text="Unsupported")

	else:
		statusLabel.config(text="Supported")

root = Tkinter.Tk()

root.after(1, checkOS)

statusLabel = Tkinter.Label(root, text="Status Label")

sizeLabel = Tkinter.Label(root, text="Size")
sizeEntry = Tkinter.Label(root)
sizeUnit = Tkinter.StringVar(root)
sizeUnit.set("MB")
sizeDropdown = Tkinter.OptionMenu(root, sizeUnit, "MB", "GB")

sizeLabel.grid(column=0, row = 0)
sizeEntry.grid(column=1, row = 0)
sizeDropDown.grid(column = 2, row = 0)

root.mainloop()


