from PIL import Image

#path = "/root/Documents/coding/coding/kucing.jpg"
#img = Image.open(path)
#width, height = img.size

getpixXpos = 0
getpixYpos = 0
pixX = 0
pixY = 0
minX = 0
maxX = 0
minY = 0
maxY = 0

#getpixel(col, row)

def getpixelcoord(path):
    img = Image.open(path)
    width, height = img.size
    
    global getpixXpos
    global getpixYpos
    global pixX
    global pixY
    global minX
    global maxX
    global minY
    global maxY
     
    while True:
        try:
            while True:
                pixX = img.getpixel((getpixXpos, getpixYpos))
                getpixXpos = getpixXpos - 1
                #print("current X position = " + str(getpixXpos))
        except:
            minX = getpixXpos + 1
            print("Position " + str(minX) + " ... and stop")
            print("Minimum X Position = " + str(getpixXpos + 1))
            print("Minimum X Value = " + str(pixX))
            break

    getpixXpos = 0
    
    while True:
        try:
            while True:
                pixX = img.getpixel((getpixXpos, getpixYpos))
                getpixXpos = getpixXpos + 1
                #print("current X position = " + str(getpixXpos))
        except:
            maxX = getpixXpos - 1
            print("Position " + str(maxX) + " ... and stop")
            print("Maximum X Position = " + str(getpixXpos - 1))
            print("Maximum X Value = " + str(pixX))
            break

    getpixXpos = 0

    #print("current X = " + str(getpixXpos))
    #print("current Y = " + str(getpixYpos))

    while True:
        try:
            while True:
                pixY = img.getpixel((getpixXpos, getpixYpos))
                getpixYpos = getpixYpos - 1
                #print("current Y position = " + str(getpixXpos))
        except:#Exception as error:
            #print(repr(error))
            minY = getpixYpos + 1
            print("Position " + str(minY) + " ... and stop")
            print("Minimum Y Position = " + str(getpixYpos + 1))
            print("Minimum Y Value = " + str(pixY))
            break

    getpixYpos = 0

    while True:
        try:
            while True:
                pixY = img.getpixel((getpixXpos, getpixYpos))
                getpixYpos = getpixYpos + 1
                #print("current Y position = " + str(getpixXpos))
        except:
            maxY = getpixYpos - 1
            print("Position " + str(maxY) + " ... and stop")
            print("Maximum Y Position = " + str(getpixYpos - 1))
            print("Maximum Y Value = " + str(pixY))
            break

    getpixYpos = 0

    print("Minimum pixel coordinate = " + "(" + str(minX) + "," + str(minY) + ")")
    print("Maximum pixel coordinate = " + "(" + str(maxX) + "," + str(maxY) + ")")

    return minX, minY, maxX, maxY

def main():
    return
    #getpixelcoord(img)

if __name__ == "__main__":
    main()
    print("The job get done!")
