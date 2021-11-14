def body_coord(arg):
    switcher = {
        "Teeth":"9 10",
        "Chest":"11 12 23 24",
        "Right Arm":"12 14 16 18 20 22",
        "Left Arm":"11 13 15 17 19 21",
        "Right Hand":"16 18 20 22",
        "Left Hand":"15 17 19 21",
        "Right Shoulder":"12",
        "Left Shoulder":"11",
        "Pelvis":"23 24",
        "Right Thigh":"24 26",
        "Left Thigh":"23 25",
        "Right Leg":"24 26 28 30 32",
        "Left Leg":"23 25 27 29 31",
        "Right Knee":"26",
        "Left Knee":"25",
        "Right Ankle":"28 30 32",
        "Left Ankle":"27 29 31",
        "Right Foot":"28 30 32",
        "Left Foot":"27 29 31"
    }

    for i in switcher:
        if i == arg:
            l = switcher[i].split()
            count = 0
            for j in l:
                l[count] = int(j)
                count = count + 1
            return(l)
