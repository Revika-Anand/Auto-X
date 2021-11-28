import detection
from tkinter import messagebox

lm = detection.landmarks           # contains the coordinates of all the joints and their visibility
req_coord = detection.coords       # contains the list of indexes of joints coordinates required
visi_list = list()                 # will contain the visibilty of all the required joints
rq_coord_list = list()             # will contain the x, y and z coordinate of all the required joints

for i in req_coord:
    l = list()
    x = lm[i].x
    y = lm[i].y
    z = lm[i].z
    l.append(x)
    l.append(y)
    l.append(z)
    rq_coord_list.append(l)
    visi_list.append(lm[i].visibility)

for i in visi_list:               # checks if the required joints are visible or not
    if i > 0.8:
        pass
    else:
        messagebox.showerror("Error", "Required joints not visible")
        quit()

messagebox.showinfo("Success", "Required joints are visible X-ray will be taken shortly please do not move")
#print(rq_coord_list)


# rq_coord_list can be forwarded to an x-ray machine which can adjust itself according to the coordinates
# mentioned and the x-ray can be taken