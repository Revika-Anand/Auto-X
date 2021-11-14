import detection
from tkinter import messagebox

lm = detection.landmarks
req_coord = detection.coords
rc_list = list()

for i in req_coord:
    rc_list.append(lm[i].visibility)

for i in rc_list:
    if i > 0.8:
        pass
    else:
        messagebox.showerror("Error", "Required joints not visible")
        quit()

messagebox.showinfo("Success", "Required joints are visible X-ray will be taken shortly please do not move")