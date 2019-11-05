from PIL import Image
import numpy

#path = "/root/Documents/coding/coding/kucing.jpg"
#Image = Image.open(path)
#width, height = Image.size

def gaussian(source, color_method, minX, minY, maxX, maxY):
    width, height = source.size

    kernel_gaussian = numpy.array([[1/339, 5/339, 7/339, 5/339, 1/339],\
                                [5/339, 20/339, 33/339, 20/339, 5/339],\
                                [7/339, 33/339, 55/339, 33/339, 7/339],\
                                [5/339, 20/339, 33/339, 20/339, 5/339],\
                                [1/339, 5/339, 7/339, 5/339, 1/339]])
    
    ############################## PIL IMAGE
    ## color image = RGB
    ## grayscale image = LA
    ## black and white = 1
    ########################################

    if color_method == "RGB":
        newImage = Image.new("RGB",(width,height), "white")
    else:
        newImage = Image.new("L",(width,height), "white")

    ##### ---------------- kolom // width = lebar
    for i in range(0+2,maxX-1):#, 2):
        ##### ------------  baris // height = tinggi
        for j in range(0+2,maxY-1):#, 2):
            if color_method == "RGB":
                sumR = sumG = sumB = R = G = B = 0
                #print(sumR, sumG, sumB, R, G, B)
                R, G, B = source.getpixel((i-2, j-2))
                sumR = sumR + (kernel_gaussian[0][0] * R)
                sumG = sumG + (kernel_gaussian[0][0] * G)
                sumB = sumB + (kernel_gaussian[0][0] * B)
                R, G, B = source.getpixel((i-2, j-1))
                sumR = sumR + (kernel_gaussian[0][1] * R)
                sumG = sumG + (kernel_gaussian[0][1] * G)
                sumB = sumB + (kernel_gaussian[0][1] * B)
                R, G, B = source.getpixel((i-2, j))
                sumR = sumR + (kernel_gaussian[0][2] * R)
                sumG = sumG + (kernel_gaussian[0][2] * G)
                sumB = sumB + (kernel_gaussian[0][2] * B)
                R, G, B = source.getpixel((i-2, j+1))
                sumR = sumR + (kernel_gaussian[0][3] * R)
                sumG = sumG + (kernel_gaussian[0][3] * G)
                sumB = sumB + (kernel_gaussian[0][3] * B)
                R, G, B = source.getpixel((i-2, j+2))
                sumR = sumR + (kernel_gaussian[0][4] * R)
                sumG = sumG + (kernel_gaussian[0][4] * G)
                sumB = sumB + (kernel_gaussian[0][4] * B)
                R, G, B = source.getpixel((i-1, j-2))
                sumR = sumR + (kernel_gaussian[1][0] * R)
                sumG = sumG + (kernel_gaussian[1][0] * G)
                sumB = sumB + (kernel_gaussian[1][0] * B)
                R, G, B = source.getpixel((i-1, j-1))
                sumR = sumR + (kernel_gaussian[1][1] * R)
                sumG = sumG + (kernel_gaussian[1][1] * G)
                sumB = sumB + (kernel_gaussian[1][1] * B)
                R, G, B = source.getpixel((i-1, j))
                sumR = sumR + (kernel_gaussian[1][2] * R)
                sumG = sumG + (kernel_gaussian[1][2] * G)
                sumB = sumB + (kernel_gaussian[1][2] * B)
                R, G, B = source.getpixel((i-1, j+1))
                sumR = sumR + (kernel_gaussian[1][3] * R)
                sumG = sumG + (kernel_gaussian[1][3] * G)
                sumB = sumB + (kernel_gaussian[1][3] * B)
                R, G, B = source.getpixel((i-1, j+2))
                sumR = sumR + (kernel_gaussian[1][4] * R)
                sumG = sumG + (kernel_gaussian[1][4] * G)
                sumB = sumB + (kernel_gaussian[1][4] * B)
                R, G, B = source.getpixel((i, j-2))
                sumR = sumR + (kernel_gaussian[2][0] * R)
                sumG = sumG + (kernel_gaussian[2][0] * G)
                sumB = sumB + (kernel_gaussian[2][0] * B)
                R, G, B = source.getpixel((i, j-1))
                sumR = sumR + (kernel_gaussian[2][1] * R)
                sumG = sumG + (kernel_gaussian[2][1] * G)
                sumB = sumB + (kernel_gaussian[2][1] * B)
                R, G, B = source.getpixel((i, j))
                sumR = sumR + (kernel_gaussian[2][2] * R)
                sumG = sumG + (kernel_gaussian[2][2] * G)
                sumB = sumB + (kernel_gaussian[2][2] * B)
                R, G, B = source.getpixel((i, j+1))
                sumR = sumR + (kernel_gaussian[2][3] * R)
                sumG = sumG + (kernel_gaussian[2][3] * G)
                sumB = sumB + (kernel_gaussian[2][3] * B)
                R, G, B = source.getpixel((i, j+2)) 
                sumR = sumR + (kernel_gaussian[2][4] * R)
                sumG = sumG + (kernel_gaussian[2][4] * G)
                sumB = sumB + (kernel_gaussian[2][4] * B)
                R, G, B = source.getpixel((i+1, j-2))
                sumR = sumR + (kernel_gaussian[3][0] * R)
                sumG = sumG + (kernel_gaussian[3][0] * G)
                sumB = sumB + (kernel_gaussian[3][0] * B)
                R, G, B = source.getpixel((i+1, j-1))
                sumR = sumR + (kernel_gaussian[3][1] * R)
                sumG = sumG + (kernel_gaussian[3][1] * G)
                sumB = sumB + (kernel_gaussian[3][1] * B)
                R, G, B = source.getpixel((i+1, j))
                sumR = sumR + (kernel_gaussian[3][2] * R)
                sumG = sumG + (kernel_gaussian[3][2] * G)
                sumB = sumB + (kernel_gaussian[3][2] * B)
                R, G, B = source.getpixel((i+1, j+1))
                sumR = sumR + (kernel_gaussian[3][3] * R)
                sumG = sumG + (kernel_gaussian[3][3] * G)
                sumB = sumB + (kernel_gaussian[3][3] * B)
                R, G, B = source.getpixel((i+1, j+2))
                sumR = sumR + (kernel_gaussian[3][4] * R)
                sumG = sumG + (kernel_gaussian[3][4] * G)
                sumB = sumB + (kernel_gaussian[3][4] * B)
                R, G, B = source.getpixel((i+2, j-2))
                sumR = sumR + (kernel_gaussian[4][0] * R)
                sumG = sumG + (kernel_gaussian[4][0] * G)
                sumB = sumB + (kernel_gaussian[4][0] * B)
                R, G, B = source.getpixel((i+2, j-1))
                sumR = sumR + (kernel_gaussian[4][1] * R)
                sumG = sumG + (kernel_gaussian[4][1] * G)
                sumB = sumB + (kernel_gaussian[4][1] * B)
                R, G, B = source.getpixel((i+2, j))
                sumR = sumR + (kernel_gaussian[4][2] * R)
                sumG = sumG + (kernel_gaussian[4][2] * G)
                sumB = sumB + (kernel_gaussian[4][2] * B)
                R, G, B = source.getpixel((i+2, j+1))
                sumR = sumR + (kernel_gaussian[4][3] * R)
                sumG = sumG + (kernel_gaussian[4][3] * G)
                sumB = sumB + (kernel_gaussian[4][3] * B)
                R, G, B = source.getpixel((i+2, j+2))
                sumR = sumR + (kernel_gaussian[4][4] * R)
                sumG = sumG + (kernel_gaussian[4][4] * G)
                sumB = sumB + (kernel_gaussian[4][4] * B)

                #print("R = " + str(sumR) + "\nG = " + str(sumG) + "\nB = " + str(sumB))

                intR, intG, intB = int(sumR), int(sumG), int(sumB)            
                if intR > 255: intR = 255
                elif intR < 0: intR = 0
                else: pass
                if intG > 255: intG = 255
                elif intG < 0: intG = 0
                else: pass
                if intB > 255: intB = 255
                elif intB < 0: intB = 0
                else: pass

                #print("R = " + str(intR) + "\nG = " + str(intG) + "\nB = " + str(intB))
                newImage.putpixel((i,j),(intR, intG, intB))
            else:
                sumBW = BW = 0

                BW = source.getpixel((i-2, j-2))
                sumBW = sumBW + (kernel_gaussian[0][0] * BW)
                BW = source.getpixel((i-2, j-1))
                sumBW = sumBW + (kernel_gaussian[0][1] * BW)
                BW = source.getpixel((i-2, j))
                sumBW = sumBW + (kernel_gaussian[0][2] * BW)
                BW = source.getpixel((i-2, j+1))
                sumBW = sumBW + (kernel_gaussian[0][3] * BW)
                BW = source.getpixel((i-2, j+2))
                sumBW = sumBW + (kernel_gaussian[0][4] * BW)
                BW = source.getpixel((i-1, j-2))
                sumBW = sumBW + (kernel_gaussian[1][0] * BW)
                BW = source.getpixel((i-1, j-1))
                sumBW = sumBW + (kernel_gaussian[1][1] * BW)
                BW = source.getpixel((i-1, j))
                sumBW = sumBW + (kernel_gaussian[1][2] * BW)
                BW = source.getpixel((i-1, j+1))
                sumBW = sumBW + (kernel_gaussian[1][3] * BW)
                BW = source.getpixel((i-1, j+2))
                sumBW = sumBW + (kernel_gaussian[1][4] * BW)
                BW = source.getpixel((i, j-2))
                sumBW = sumBW + (kernel_gaussian[2][0] * BW)
                BW = source.getpixel((i, j-1))
                sumBW = sumBW + (kernel_gaussian[2][1] * BW)
                BW = source.getpixel((i, j))
                sumBW = sumBW + (kernel_gaussian[2][2] * BW)
                BW = source.getpixel((i, j+1))
                sumBW = sumBW + (kernel_gaussian[2][3] * BW)
                BW = source.getpixel((i, j+2)) 
                sumBW = sumBW + (kernel_gaussian[2][4] * BW)
                BW = source.getpixel((i+1, j-2))
                sumBW = sumBW + (kernel_gaussian[3][0] * BW)
                BW = source.getpixel((i+1, j-1))
                sumBW = sumBW + (kernel_gaussian[3][1] * BW)
                BW = source.getpixel((i+1, j))
                sumBW = sumBW + (kernel_gaussian[3][2] * BW)
                BW = source.getpixel((i+1, j+1))
                sumBW = sumBW + (kernel_gaussian[3][3] * BW)
                BW = source.getpixel((i+1, j+2))
                sumBW = sumBW + (kernel_gaussian[3][4] * BW)
                BW = source.getpixel((i+2, j-2))
                sumBW = sumBW + (kernel_gaussian[4][0] * BW)
                BW = source.getpixel((i+2, j-1))
                sumBW = sumBW + (kernel_gaussian[4][1] * BW)
                BW = source.getpixel((i+2, j))
                sumBW = sumBW + (kernel_gaussian[4][2] * BW)
                BW = source.getpixel((i+2, j+1))
                sumBW = sumBW + (kernel_gaussian[4][3] * BW)
                BW = source.getpixel((i+2, j+2))
                sumBW = sumBW + (kernel_gaussian[4][4] * BW)

                intBW = int(sumBW)            
                if intBW > 255: intBW = 255
                elif intBW < 0: intBW = 0
                else: pass

                newImage.putpixel((i,j),(intBW))
    return newImage

def Canny(source, color_method, minX, minY, maxX, maxY):
    width, height = source.size

    kernel_canny_X = numpy.array([[-1, 0, 1],
                                [-2, 0, 2],
                                [-1, 0, 1]])

    kernel_canny_Y = numpy.array([[-1, -2, -1],
                                [0, 0, 0],
                                [1, 2, 1]])

    if color_method == "RGB":
        newImage = Image.new("RGB",(width,height), "white")
    else:
        newImage = Image.new("L",(width,height), "white")

    sumValR = sumValG = sumValB = powR = powG = powB = 0
    sumValB = sumValW = powB = powW = 0
    sumValBW = powBW = 0

    ##### ---------------- kolom // width = lebar
    for i in range(0+1,maxX):#, 2):
        ##### ------------  baris // height = tinggi
        for j in range(0+1,maxY):#, 2):
            if color_method == "RGB":
                sumRx = sumGx = sumBx = sumRy = sumGy = sumBy = R = G = B = 0
                #print(sumR, sumG, sumB, R, G, B)
                R, G, B = source.getpixel((i-1, j-1))
                sumRx = sumRx + (kernel_canny_X[0][0] * R)
                sumGx = sumGx + (kernel_canny_X[0][0] * G)
                sumBx = sumBx + (kernel_canny_X[0][0] * B)
                sumRy = sumRy + (kernel_canny_Y[0][0] * R)
                sumGy = sumGy + (kernel_canny_Y[0][0] * G)
                sumBy = sumBy + (kernel_canny_Y[0][0] * B)
                R, G, B = source.getpixel((i-1, j))
                sumRx = sumRx + (kernel_canny_X[0][1] * R)
                sumGx = sumGx + (kernel_canny_X[0][1] * G)
                sumBx = sumBx + (kernel_canny_X[0][1] * B)
                sumRy = sumRy + (kernel_canny_Y[0][1] * R)
                sumGy = sumGy + (kernel_canny_Y[0][1] * G)
                sumBy = sumBy + (kernel_canny_Y[0][1] * B)
                R, G, B = source.getpixel((i-1, j+1))
                sumRx = sumRx + (kernel_canny_X[0][2] * R)
                sumGx = sumGx + (kernel_canny_X[0][2] * G)
                sumBx = sumBx + (kernel_canny_X[0][2] * B)
                sumRy = sumRy + (kernel_canny_Y[0][2] * R)
                sumGy = sumGy + (kernel_canny_Y[0][2] * G)
                sumBy = sumBy + (kernel_canny_Y[0][2] * B)
                R, G, B = source.getpixel((i, j-1))
                sumRx = sumRx + (kernel_canny_X[1][0] * R)
                sumGx = sumGx + (kernel_canny_X[1][0] * G)
                sumBx = sumBx + (kernel_canny_X[1][0] * B)
                sumRy = sumRy + (kernel_canny_Y[1][0] * R)
                sumGy = sumGy + (kernel_canny_Y[1][0] * G)
                sumBy = sumBy + (kernel_canny_Y[1][0] * B)
                R, G, B = source.getpixel((i, j))
                sumRx = sumRx + (kernel_canny_X[1][1] * R)
                sumGx = sumGx + (kernel_canny_X[1][1] * G)
                sumBx = sumBx + (kernel_canny_X[1][1] * B)
                sumRy = sumRy + (kernel_canny_Y[1][1] * R)
                sumGy = sumGy + (kernel_canny_Y[1][1] * G)
                sumBy = sumBy + (kernel_canny_Y[1][1] * B)
                R, G, B = source.getpixel((i, j+1))
                sumRx = sumRx + (kernel_canny_X[1][2] * R)
                sumGx = sumGx + (kernel_canny_X[1][2] * G)
                sumBx = sumBx + (kernel_canny_X[1][2] * B)
                sumRy = sumRy + (kernel_canny_Y[1][2] * R)
                sumGy = sumGy + (kernel_canny_Y[1][2] * G)
                sumBy = sumBy + (kernel_canny_Y[1][2] * B)
                R, G, B = source.getpixel((i+1, j-1))
                sumRx = sumRx + (kernel_canny_X[2][0] * R)
                sumGx = sumGx + (kernel_canny_X[2][0] * G)
                sumBx = sumBx + (kernel_canny_X[2][0] * B)
                sumRy = sumRy + (kernel_canny_Y[2][0] * R)
                sumGy = sumGy + (kernel_canny_Y[2][0] * G)
                sumBy = sumBy + (kernel_canny_Y[2][0] * B)
                R, G, B = source.getpixel((i+1, j))
                sumRx = sumRx + (kernel_canny_X[2][1] * R)
                sumGx = sumGx + (kernel_canny_X[2][1] * G)
                sumBx = sumBx + (kernel_canny_X[2][1] * B)
                sumRy = sumRy + (kernel_canny_Y[2][1] * R)
                sumGy = sumGy + (kernel_canny_Y[2][1] * G)
                sumBy = sumBy + (kernel_canny_Y[2][1] * B)
                R, G, B = source.getpixel((i+1, j+1))
                sumRx = sumRx + (kernel_canny_X[2][2] * R)
                sumGx = sumGx + (kernel_canny_X[2][2] * G)
                sumBx = sumBx + (kernel_canny_X[2][2] * B)
                sumRy = sumRy + (kernel_canny_Y[2][2] * R)
                sumGy = sumGy + (kernel_canny_Y[2][2] * G)
                sumBy = sumBy + (kernel_canny_Y[2][2] * B)

                sumValR = sumRx + sumRy
                sumValG = sumGx + sumGy
                sumValB = sumBx + sumBy

                #powR = sumValR**2
                #powG = sumValG**2
                #powB = sumValB**2
                #intR, intG, intB = int(powR), int(powG), int(powB)

                intR, intG, intB = int(sumValR), int(sumValG), int(sumValB)            
                if intR > 255: intR = 255
                elif intR < 0: intR = 0
                else: pass
                if intG > 255: intG = 255
                elif intG < 0: intG = 0
                else: pass
                if intB > 255: intB = 255
                elif intB < 0: intB = 0
                else: pass

                newImage.putpixel((i,j),(intR, intG, intB))
            elif color_method == "BW":
                sumBWx = sumBWy = BW = 0

                BW = source.getpixel((i-1, j-1))
                sumBWx = sumBWx + (kernel_canny_X[0][0] * BW)
                sumBWy = sumBWy + (kernel_canny_Y[0][0] * BW)
                BW = source.getpixel((i-1, j))
                sumBWx = sumBWx + (kernel_canny_X[0][1] * BW)
                sumBWy = sumBWy + (kernel_canny_Y[0][1] * BW)
                BW = source.getpixel((i-1, j+1))
                sumBWx = sumBWx + (kernel_canny_X[0][2] * BW)
                sumBWy = sumBWy + (kernel_canny_Y[0][2] * BW)
                BW = source.getpixel((i, j-1))
                sumBWx = sumBWx + (kernel_canny_X[1][0] * BW)
                sumBWy = sumBWy + (kernel_canny_Y[1][0] * BW)
                BW = source.getpixel((i, j))
                sumBWx = sumBWx + (kernel_canny_X[1][1] * BW)
                sumBWy = sumBWy + (kernel_canny_Y[1][1] * BW)
                BW = source.getpixel((i, j+1))
                sumBWx = sumBWx + (kernel_canny_X[1][2] * BW)
                sumBWy = sumBWy + (kernel_canny_Y[1][2] * BW)
                BW = source.getpixel((i+1, j-1))
                sumBWx = sumBWx + (kernel_canny_X[2][0] * BW)
                sumBWy = sumBWy + (kernel_canny_Y[2][0] * BW)
                BW = source.getpixel((i+1, j))
                sumBWx = sumBWx + (kernel_canny_X[2][1] * BW)
                sumBWy = sumBWy + (kernel_canny_Y[2][1] * BW)
                BW = source.getpixel((i+1, j+1))
                sumBWx = sumBWx + (kernel_canny_X[2][2] * BW)
                sumBWy = sumBWy + (kernel_canny_Y[2][2] * BW)

                #sumValBW = abs((sumBWx**2) + (sumBWy**2))
                sumValBW = sumBWx + sumBWy

                intBW = int(sumValBW)       
                if intBW > 255: intBW = 255
                elif intBW < 0: intBW = 0
                else: pass

                newImage.putpixel((i,j),(intBW))
            else:
                sumBx = sumBy = sumWx = sumWy = B = W = 0
                
                B, W = source.getpixel((i-1, j-1))
                sumBx = sumBx + (kernel_canny_X[0][0] * B)
                sumBy = sumBy + (kernel_canny_X[0][0] * B)
                sumWx = sumWx + (kernel_canny_Y[0][0] * W)
                sumWy = sumWy + (kernel_canny_Y[0][0] * W)
                B, W = source.getpixel((i-1, j))
                sumBx = sumBx + (kernel_canny_X[0][1] * B)
                sumBy = sumBy + (kernel_canny_X[0][1] * B)
                sumWx = sumWx + (kernel_canny_Y[0][1] * W)
                sumWy = sumWy + (kernel_canny_Y[0][1] * W)
                B, W = source.getpixel((i-1, j+1))
                sumBx = sumBx + (kernel_canny_X[0][2] * B)
                sumBy = sumBy + (kernel_canny_X[0][2] * B)
                sumWx = sumWx + (kernel_canny_Y[0][2] * W)
                sumWy = sumWy + (kernel_canny_Y[0][2] * W)
                B, W = source.getpixel((i, j-1))
                sumBx = sumBx + (kernel_canny_X[1][0] * B)
                sumBy = sumBy + (kernel_canny_X[1][0] * B)
                sumWx = sumWx + (kernel_canny_Y[1][0] * W)
                sumWy = sumWy + (kernel_canny_Y[1][0] * W)
                B, W = source.getpixel((i, j))
                sumBx = sumBx + (kernel_canny_X[1][1] * B)
                sumBy = sumBy + (kernel_canny_X[1][1] * B)
                sumWx = sumWx + (kernel_canny_Y[1][1] * W)
                sumWy = sumWy + (kernel_canny_Y[1][1] * W)
                B, W = source.getpixel((i, j+1))
                sumBx = sumBx + (kernel_canny_X[1][2] * B)
                sumBy = sumBy + (kernel_canny_X[1][2] * B)
                sumWx = sumWx + (kernel_canny_Y[1][2] * W)
                sumWy = sumWy + (kernel_canny_Y[1][2] * W)
                B, W = source.getpixel((i+1, j-1))
                sumBx = sumBx + (kernel_canny_X[2][0] * B)
                sumBy = sumBy + (kernel_canny_X[2][0] * B)
                sumWx = sumWx + (kernel_canny_Y[2][0] * W)
                sumWy = sumWy + (kernel_canny_Y[2][0] * W)
                B, W = source.getpixel((i+1, j))
                sumBx = sumBx + (kernel_canny_X[2][1] * B)
                sumBy = sumBy + (kernel_canny_X[2][1] * B)
                sumWx = sumWx + (kernel_canny_Y[2][1] * W)
                sumWy = sumWy + (kernel_canny_Y[2][1] * W)
                B, W = source.getpixel((i+1, j+1))
                sumBx = sumBx + (kernel_canny_X[2][2] * B)
                sumBy = sumBy + (kernel_canny_X[2][2] * B)
                sumWx = sumWx + (kernel_canny_Y[2][2] * W)
                sumWy = sumWy + (kernel_canny_Y[2][2] * W)

                #sumValBW = abs((sumBWx**2) + (sumBWy**2))
                sumValB = sumBx + sumBy
                sumValW = sumWx + sumWy

                intB, intW = int(sumValB), int(sumValW)            
                if intB > 255: intB = 255
                elif intB < 0: intB = 0
                else: pass
                if intW > 255: intW = 255
                elif intW < 0: intW = 0
                else: pass

                newImage.putpixel((i,j),(intB, intW))
    return newImage

def prewitt(source, color_method, minX, minY, maxX, maxY):
    width, height = source.size

    kernel_prewitt_X = numpy.array([[-1, 0, 1],
                                [-1, 0, 1],
                                [-1, 0, 1]])

    kernel_prewitt_Y = numpy.array([[1, 1, 1],
                                [0, 0, 0],
                                [-1, -1, -1]])

    if color_method == "RGB":
        newImage = Image.new("RGB",(width,height), "white")
    else:
        newImage = Image.new("L",(width,height), "white")

    sumValR = sumValG = sumValB = powR = powG = powB = 0
    sumValB = sumValW = powB = powW = 0
    sumValBW = powBW = 0

    ##### ---------------- kolom // width = lebar
    for i in range(0+1,maxX):#, 2):
        ##### ------------  baris // height = tinggi
        for j in range(0+1,maxY):#, 2):
            if color_method == "RGB":
                sumRx = sumGx = sumBx = sumRy = sumGy = sumBy = R = G = B = 0
                #print(sumR, sumG, sumB, R, G, B)
                R, G, B = source.getpixel((i-1, j-1))
                sumRx = sumRx + (kernel_prewitt_X[0][0] * R)
                sumGx = sumGx + (kernel_prewitt_X[0][0] * G)
                sumBx = sumBx + (kernel_prewitt_X[0][0] * B)
                sumRy = sumRy + (kernel_prewitt_Y[0][0] * R)
                sumGy = sumGy + (kernel_prewitt_Y[0][0] * G)
                sumBy = sumBy + (kernel_prewitt_Y[0][0] * B)
                R, G, B = source.getpixel((i-1, j))
                sumRx = sumRx + (kernel_prewitt_X[0][1] * R)
                sumGx = sumGx + (kernel_prewitt_X[0][1] * G)
                sumBx = sumBx + (kernel_prewitt_X[0][1] * B)
                sumRy = sumRy + (kernel_prewitt_Y[0][1] * R)
                sumGy = sumGy + (kernel_prewitt_Y[0][1] * G)
                sumBy = sumBy + (kernel_prewitt_Y[0][1] * B)
                R, G, B = source.getpixel((i-1, j+1))
                sumRx = sumRx + (kernel_prewitt_X[0][2] * R)
                sumGx = sumGx + (kernel_prewitt_X[0][2] * G)
                sumBx = sumBx + (kernel_prewitt_X[0][2] * B)
                sumRy = sumRy + (kernel_prewitt_Y[0][2] * R)
                sumGy = sumGy + (kernel_prewitt_Y[0][2] * G)
                sumBy = sumBy + (kernel_prewitt_Y[0][2] * B)
                R, G, B = source.getpixel((i, j-1))
                sumRx = sumRx + (kernel_prewitt_X[1][0] * R)
                sumGx = sumGx + (kernel_prewitt_X[1][0] * G)
                sumBx = sumBx + (kernel_prewitt_X[1][0] * B)
                sumRy = sumRy + (kernel_prewitt_Y[1][0] * R)
                sumGy = sumGy + (kernel_prewitt_Y[1][0] * G)
                sumBy = sumBy + (kernel_prewitt_Y[1][0] * B)
                R, G, B = source.getpixel((i, j))
                sumRx = sumRx + (kernel_prewitt_X[1][1] * R)
                sumGx = sumGx + (kernel_prewitt_X[1][1] * G)
                sumBx = sumBx + (kernel_prewitt_X[1][1] * B)
                sumRy = sumRy + (kernel_prewitt_Y[1][1] * R)
                sumGy = sumGy + (kernel_prewitt_Y[1][1] * G)
                sumBy = sumBy + (kernel_prewitt_Y[1][1] * B)
                R, G, B = source.getpixel((i, j+1))
                sumRx = sumRx + (kernel_prewitt_X[1][2] * R)
                sumGx = sumGx + (kernel_prewitt_X[1][2] * G)
                sumBx = sumBx + (kernel_prewitt_X[1][2] * B)
                sumRy = sumRy + (kernel_prewitt_Y[1][2] * R)
                sumGy = sumGy + (kernel_prewitt_Y[1][2] * G)
                sumBy = sumBy + (kernel_prewitt_Y[1][2] * B)
                R, G, B = source.getpixel((i+1, j-1))
                sumRx = sumRx + (kernel_prewitt_X[2][0] * R)
                sumGx = sumGx + (kernel_prewitt_X[2][0] * G)
                sumBx = sumBx + (kernel_prewitt_X[2][0] * B)
                sumRy = sumRy + (kernel_prewitt_Y[2][0] * R)
                sumGy = sumGy + (kernel_prewitt_Y[2][0] * G)
                sumBy = sumBy + (kernel_prewitt_Y[2][0] * B)
                R, G, B = source.getpixel((i+1, j))
                sumRx = sumRx + (kernel_prewitt_X[2][1] * R)
                sumGx = sumGx + (kernel_prewitt_X[2][1] * G)
                sumBx = sumBx + (kernel_prewitt_X[2][1] * B)
                sumRy = sumRy + (kernel_prewitt_Y[2][1] * R)
                sumGy = sumGy + (kernel_prewitt_Y[2][1] * G)
                sumBy = sumBy + (kernel_prewitt_Y[2][1] * B)
                R, G, B = source.getpixel((i+1, j+1))
                sumRx = sumRx + (kernel_prewitt_X[2][2] * R)
                sumGx = sumGx + (kernel_prewitt_X[2][2] * G)
                sumBx = sumBx + (kernel_prewitt_X[2][2] * B)
                sumRy = sumRy + (kernel_prewitt_Y[2][2] * R)
                sumGy = sumGy + (kernel_prewitt_Y[2][2] * G)
                sumBy = sumBy + (kernel_prewitt_Y[2][2] * B)

                sumValR = sumRx + sumRy
                sumValG = sumGx + sumGy
                sumValB = sumBx + sumBy

                #powR = sumValR**2
                #powG = sumValG**2
                #powB = sumValB**2
                #intR, intG, intB = int(powR), int(powG), int(powB)

                intR, intG, intB = int(sumValR), int(sumValG), int(sumValB)            
                if intR > 255: intR = 255
                elif intR < 0: intR = 0
                else: pass
                if intG > 255: intG = 255
                elif intG < 0: intG = 0
                else: pass
                if intB > 255: intB = 255
                elif intB < 0: intB = 0
                else: pass

                newImage.putpixel((i,j),(intR, intG, intB))
            else:
                sumBWx = sumBWy = BW = 0
                
                BW = source.getpixel((i-1, j-1))
                sumBWx = sumBWx + (kernel_prewitt_X[0][0] * BW)
                sumBWy = sumBWy + (kernel_prewitt_Y[0][0] * BW)
                BW = source.getpixel((i-1, j))
                sumBWx = sumBWx + (kernel_prewitt_X[0][1] * BW)
                sumBWy = sumBWy + (kernel_prewitt_Y[0][1] * BW)
                BW = source.getpixel((i-1, j+1))
                sumBWx = sumBWx + (kernel_prewitt_X[0][2] * BW)
                sumBWy = sumBWy + (kernel_prewitt_Y[0][2] * BW)
                BW = source.getpixel((i, j-1))
                sumBWx = sumBWx + (kernel_prewitt_X[1][0] * BW)
                sumBWy = sumBWy + (kernel_prewitt_Y[1][0] * BW)
                BW = source.getpixel((i, j))
                sumBWx = sumBWx + (kernel_prewitt_X[1][1] * BW)
                sumBWy = sumBWy + (kernel_prewitt_Y[1][1] * BW)
                BW = source.getpixel((i, j+1))
                sumBWx = sumBWx + (kernel_prewitt_X[1][2] * BW)
                sumBWy = sumBWy + (kernel_prewitt_Y[1][2] * BW)
                BW = source.getpixel((i+1, j-1))
                sumBWx = sumBWx + (kernel_prewitt_X[2][0] * BW)
                sumBWy = sumBWy + (kernel_prewitt_Y[2][0] * BW)
                BW = source.getpixel((i+1, j))
                sumBWx = sumBWx + (kernel_prewitt_X[2][1] * BW)
                sumBWy = sumBWy + (kernel_prewitt_Y[2][1] * BW)
                BW = source.getpixel((i+1, j+1))
                sumBWx = sumBWx + (kernel_prewitt_X[2][2] * BW)
                sumBWy = sumBWy + (kernel_prewitt_Y[2][2] * BW)

                #sumValBW = abs((sumBWx**2) + (sumBWy**2))
                sumValBW = sumBWx + sumBWy

                intBW = int(sumValBW)            
                if intBW > 255: intBW = 255
                elif intBW < 0: intBW = 0
                else: pass

                newImage.putpixel((i,j),(intBW))
    return newImage

def robert(source, color_method, minX, minY, maxX, maxY):
    width, height = source.size

    kernel_robert_X = numpy.array([[1, 0],
                                [0, -1]])

    kernel_robert_Y = numpy.array([[0, 1],
                                [-1, 0]])

    if color_method == "RGB":
        newImage = Image.new("RGB",(width,height), "white")
    else:
        newImage = Image.new("L",(width,height), "white")

    sumValR = sumValG = sumValB = powR = powG = powB = 0
    sumValB = sumValW = powB = powW = 0
    sumValBW = powBW = 0

    ##### ---------------- kolom // width = lebar
    for i in range(0+1,maxX):#, 2):
        ##### ------------  baris // height = tinggi
        for j in range(0+1,maxY):#, 2):
            if color_method == "RGB":
                sumRx = sumGx = sumBx = sumRy = sumGy = sumBy = R = G = B = 0
                #print(sumR, sumG, sumB, R, G, B)
                R, G, B = source.getpixel((i-1, j-1))
                sumRx = sumRx + (kernel_robert_X[0][0] * R)
                sumGx = sumGx + (kernel_robert_X[0][0] * G)
                sumBx = sumBx + (kernel_robert_X[0][0] * B)
                sumRy = sumRy + (kernel_robert_Y[0][0] * R)
                sumGy = sumGy + (kernel_robert_Y[0][0] * G)
                sumBy = sumBy + (kernel_robert_Y[0][0] * B)
                R, G, B = source.getpixel((i-1, j))
                sumRx = sumRx + (kernel_robert_X[0][1] * R)
                sumGx = sumGx + (kernel_robert_X[0][1] * G)
                sumBx = sumBx + (kernel_robert_X[0][1] * B)
                sumRy = sumRy + (kernel_robert_Y[0][1] * R)
                sumGy = sumGy + (kernel_robert_Y[0][1] * G)
                sumBy = sumBy + (kernel_robert_Y[0][1] * B)
                R, G, B = source.getpixel((i, j-1))
                sumRx = sumRx + (kernel_robert_X[1][0] * R)
                sumGx = sumGx + (kernel_robert_X[1][0] * G)
                sumBx = sumBx + (kernel_robert_X[1][0] * B)
                sumRy = sumRy + (kernel_robert_Y[1][0] * R)
                sumGy = sumGy + (kernel_robert_Y[1][0] * G)
                sumBy = sumBy + (kernel_robert_Y[1][0] * B)
                R, G, B = source.getpixel((i, j))
                sumRx = sumRx + (kernel_robert_X[1][1] * R)
                sumGx = sumGx + (kernel_robert_X[1][1] * G)
                sumBx = sumBx + (kernel_robert_X[1][1] * B)
                sumRy = sumRy + (kernel_robert_Y[1][1] * R)
                sumGy = sumGy + (kernel_robert_Y[1][1] * G)
                sumBy = sumBy + (kernel_robert_Y[1][1] * B)

                sumValR = sumRx + sumRy
                sumValG = sumGx + sumGy
                sumValB = sumBx + sumBy

                #powR = sumValR**2
                #powG = sumValG**2
                #powB = sumValB**2
                #intR, intG, intB = int(powR), int(powG), int(powB)

                intR, intG, intB = int(sumValR), int(sumValG), int(sumValB)            
                if intR > 255: intR = 255
                elif intR < 0: intR = 0
                else: pass
                if intG > 255: intG = 255
                elif intG < 0: intG = 0
                else: pass
                if intB > 255: intB = 255
                elif intB < 0: intB = 0
                else: pass

                newImage.putpixel((i,j),(intR, intG, intB))
            else:
                sumBWx = sumBWy = BW = 0
                
                BW = source.getpixel((i-1, j-1))
                sumBWx = sumBWx + (kernel_robert_X[0][0] * BW)
                sumBWy = sumBWy + (kernel_robert_Y[0][0] * BW)
                BW = source.getpixel((i-1, j))
                sumBWx = sumBWx + (kernel_robert_X[0][1] * BW)
                sumBWy = sumBWy + (kernel_robert_Y[0][1] * BW)
                BW = source.getpixel((i, j-1))
                sumBWx = sumBWx + (kernel_robert_X[1][0] * BW)
                sumBWy = sumBWy + (kernel_robert_Y[1][0] * BW)
                BW = source.getpixel((i, j))
                sumBWx = sumBWx + (kernel_robert_X[1][1] * BW)
                sumBWy = sumBWy + (kernel_robert_Y[1][1] * BW)

                sumValBW = sumBWx + sumBWy

                #powBW = sumValBW**2
                #intBW = int(powBW)

                intBW = int(sumValBW)            
                if intBW > 255: intBW = 255
                elif intBW < 0: intBW = 0
                else: pass

                newImage.putpixel((i,j),(intBW))
    return newImage

def main():
    return
    #gaussian()

if __name__ == "__main__":
    main()
    print("The job get done!")