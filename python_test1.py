def triangle(height):
    for height_index in range(1, height+1):
        # button line
        if height_index == height:
            print("*"*(height+height_index-1))
        # other line
        elif height_index > 1:
            print(" "*(height-height_index) + "*" + " "*((height_index-1)*2-1) + "*")
        # top line
        else:
            print(" "*(height-1) + "*"*(height_index))

triangle(3)
