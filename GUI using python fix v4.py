#region Lib import
import datetime
import time
import tkinter as tk
from tkinter import HORIZONTAL as hrzntl
from tkinter import filedialog as dialogbox
from tkinter import messagebox as msgboxshw
from tkinter import ttk as ttk
from tkinter.ttk import *

import cv2 as cv
import numpy as np
from PIL import Image as img
from PIL import ImageTk as imgtk

import convolution as convolv
import getpixelcoordinate as getpix

#endregion

#region "VARIABLE"
image = ""
imagegsc = ""
imagebw = ""
locate = ""
locategsc = ""
locatebw = ""
locateFilter = ""
locategscFilter = ""
locatebwFilter = ""
window = ""
tab1 = ""
tab2 = ""
timeLabel = ""
timeLabel1 = ""
timeLabel2 = ""
comboboxlabelconvolution = ""
comboboxconvolution = ""
btncomboboxconvolution = ""
back = ""
save = ""
remove = ""
comboboxlabelgsc = ""
btncomboboxgsc = ""
cam = ""
cam_window = ""
frame = ""
btncam = ""
btnoffcam = ""
btnimg = ""
gmbr = ""
gsc = ""
blackAndWhiteImage = ""
usecam = False
useimg = False
trackContrast = ""
btncontrast = ""
trackBrightness = ""
btnbrightness = ""
contrastValue = ""
brightnessValue = ""
saveorig = ""
savegsv = ""
savebw = ""
gmbrcompress = ""
gmbrasli = ""
image = ""
imagegsc = ""
gmbrgsc = ""
gsccompress = ""
imagebw = ""
gmbrbw = ""
btnreset = ""
btncombine = ""
enablereset = False
blackAndWhiteImagecompress = ""
update_gmbr = ""
update_gsc = ""
update_bw = ""
grayscaleValue = ["PAL and NTSC", "HDTV", "HDR", "Average"]
filtermode = ["Filter Limit MinMax", "Filter Mean", "Filter Median"]
convolutionmode = ["Gaussian", "Canny", "Prewitt", "Robert"]
checkState = [False, False, False, False]
comboboxgsc = ""
comboboxfilter = ""
PAL = True
HDTV= False
HDR = False
Average = False
path = ""
filename = ""
filecam = ""
width, height = 800, 600
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
#endregion

def combine():
    global gmbr
    global gsc
    global blackAndWhiteImage
    global contrastValue
    global brightnessValue
    global gmbrcompress
    global gmbrasli
    global image
    global locategsc
    global locate
    global locatebw
    global imagegsc
    global gmbrgsc
    global gsccompress
    global imagebw
    global gmbrbw
    global blackAndWhiteImagecompress
    global update_gmbr
    global update_gsc
    global update_bw

    ###################### CONTRAST ORIGINAL ###############################
    gmbrcombine = np.int16(gmbr)
    gmbrcombine = gmbrcombine * (contrastValue/100+1) - contrastValue + brightnessValue
    gmbrcombine = np.clip(gmbrcombine, 0, 255)
    gmbrcombine = np.uint8(gmbrcombine)
    update_gmbr = img.fromarray(gmbrcombine)
    gmbrcompress = update_gmbr.resize((320, 240), img.ANTIALIAS)
    image = imgtk.PhotoImage(image=gmbrcompress)
    locate.config(image=image)

    ###################### CONTRAST GRAYSCALE ##################################
    gmbrcombinegsc = np.int16(gsc)
    gmbrcombinegsc = gmbrcombinegsc * (contrastValue/100+1) - contrastValue + brightnessValue
    gmbrcombinegsc = np.clip(gmbrcombinegsc, 0, 255)
    gmbrcombinegsc = np.uint8(gmbrcombinegsc)
    update_gsc = img.fromarray(gmbrcombinegsc)
    gsccompress = update_gsc.resize((320, 240), img.ANTIALIAS)
    imagegsc = imgtk.PhotoImage(image=gsccompress)
    locategsc.config(image=imagegsc)

    ###################### CONTRAST BW #################################
    gmbrcombinebw = np.int16(blackAndWhiteImage)
    gmbrcombinebw = gmbrcombinebw * (contrastValue/100+1) - contrastValue + brightnessValue
    gmbrcombinebw = np.clip(gmbrcombinebw, 0, 255)
    gmbrcombinebw = np.uint8(gmbrcombinebw)
    update_bw = img.fromarray(gmbrcombinebw)
    blackAndWhiteImagecompress = update_bw.resize((320, 240), img.ANTIALIAS)
    imagebw = imgtk.PhotoImage(image=blackAndWhiteImagecompress)
    locatebw.config(image=imagebw)

def convert_value():
    global grayscaleValue
    global PAL
    global HDTV
    global HDR
    global Average
    global comboboxgsc
    global locategsc
    global gsc
    global imagegsc
    global gmbrgsc
    global gsccompress
    global update_gsc
    global path
    global trackContrast
    global trackBrightness

    trackContrast.set(0)
    trackBrightness.set(0)

    if(comboboxgsc.get() == grayscaleValue[0]): #msgboxshw.showinfo("Debug", str(combobox.get()))
        PAL = True
        HDTV= False
        HDR = False
        Average = False
    elif(comboboxgsc.get() == grayscaleValue[1]):
        PAL = False
        HDTV= True
        HDR = False
        Average = False
    elif(comboboxgsc.get() == grayscaleValue[2]):
        PAL = False
        HDTV= False
        HDR = True
        Average = False
    else:
        PAL = False
        HDTV= False
        HDR = False
        Average = True

    #gray_path = img.fromarray(path)
    gsc = convert_grayscale(path)
    update_gsc = gsc
    gsccompress = gsc.resize((320, 240), img.ANTIALIAS)
    imagegsc = imgtk.PhotoImage(image=gsccompress)
    locategsc.config(image=imagegsc)

def loading_bar(val):
    progress['value']=val
    loading_window.update_idletasks()
    loading_window.update()
    time.sleep(1)

def unclosable():
    pass

def destroy_wndw():
    loading_window.destroy()

def cnvrtnc_destroy(buttonclicked):
    global btnConvertOnceFilter
    global btnConvertOnceConvolutional
    global singleconversionfilterbtn
    global singleconversionconvolutionalbtn
    
    if buttonclicked[0]:
        try: singleconversionfilterbtn.config(state="normal")
        except: pass
        return
    
    if buttonclicked[1]:
        try: btnConvertOnceFilter.config(state="normal")
        except: pass
        return
    
    if buttonclicked[2]:
        try: singleconversionconvolutionalbtn.config(state="normal")
        except: pass
        return
    
    if buttonclicked[3]:
        try: btnConvertOnceConvolutional.config(state="normal")
        except: pass
        return

def limit_filter_method(source, color_method, minX, minY, maxX, maxY):
    width, height=source.size
    members = [(0,0)] * 8
    limit = [(0,0)]
    minVal = [(0,0)]
    maxVal = [(0,0)]

    ############################## PIL IMAGE
    ## color image = RGB
    ## grayscale image = LA
    ## black and white = 1
    ########################################

    if color_method == "RGB":
        newimg = img.new("RGB",(width,height), "white")
    else:
        newimg = img.new("L",(width,height), "white")
    
    ##### ---------------- kolom // width = lebar
    for i in range(0,maxX+1):
        ##### ------------  baris // height = tinggi
        for j in range(0,maxY+1):
            try:
                members[0] = source.getpixel((i-1,j-1)) #pixel baris 1 kolom 1
            except:
                if color_method == "RGB": members[0] = (0,0,0)
                else: members[0] = 0

            try:
                members[1] = source.getpixel((i-1,j))   #pixel baris 1 kolom 2
            except:
                if color_method == "RGB": members[1] = (0,0,0)
                else: members[1] = 0

            try:
                members[2] = source.getpixel((i-1,j+1)) #pixel baris 1 kolom 3
            except:
                if color_method == "RGB": members[2] = (0,0,0)
                else: members[2] = 0

            try:
                members[3] = source.getpixel((i,j-1))   #pixel baris 2 kolom 1
            except:
                if color_method == "RGB": members[3] = (0,0,0)
                else: members[3] = 0

            limit[0] = source.getpixel((i,j))         #pixel baris 2 kolom 2 ==================== PIXEL ANALISA

            try:
                members[4] = source.getpixel((i,j+1))   #pixel baris 2 kolom 3
            except:
                if color_method == "RGB": members[4] = (0,0,0)
                else: members[4] = 0

            try:
                members[5] = source.getpixel((i+1,j-1)) #pixel baris 3 kolom 1
            except:
                if color_method == "RGB": members[5] = (0,0,0)
                else: members[5] = 0

            try:
                members[6] = source.getpixel((i+1,j))   #pixel baris 3 kolom 2
            except:
                if color_method == "RGB": members[6] = (0,0,0)
                else: members[6] = 0

            try:
                members[7] = source.getpixel((i+1,j+1)) #pixel baris 3 kolom 3
            except:
                if color_method == "RGB": members[7] = (0,0,0)
                else: members[7] = 0

            minVal[0] = min(members)
            maxVal[0] = max(members)

            if limit < minVal: newimg.putpixel((i,j),(minVal[0]))
            elif limit > maxVal: newimg.putpixel((i,j),(maxVal[0]))
            else: newimg.putpixel((i,j),(limit[0]))
    
    return newimg

def limit_proccess(filename, filecam):
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global timeLabel
    global loading_window
    global progress

    val = 0

    start = datetime.datetime.now()

    ######################## RGB
    try:
        if useimg:
            gmbrorig = img.open(filename).convert("RGB")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam).convert("RGB")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        rgb_filter = "RGB"
        limitimg = limit_filter_method(gmbrorig, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = limitimg.resize((320, 240), img.ANTIALIAS)

        image = imgtk.PhotoImage(image=gmbrasli)
        locateFilter = tk.Label(image=image)
        locateFilter.Image = image
        locateFilter.place(x=25, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Limit Proccess -> RGB image, Failed")

    val = val + 30
    loading_bar(val)

    ####################### GRAYSCALE
    try:
        if useimg:
            gmbrorig = img.open(filename)#.convert("LA")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam)#.convert("LA")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        #rgb_filter = "GSC"
        gmbrgsc = convert_grayscale(gmbrorig)
        rgb_filter = "RGB"
        limitimg = limit_filter_method(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = limitimg.resize((320, 240), img.ANTIALIAS)
        
        image = imgtk.PhotoImage(image=gmbrasli)
        locategscFilter = tk.Label(image=image)
        locategscFilter.Image = image
        locategscFilter.place(x=375, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Limit Proccess -> Grayscale image, Failed")

    val = val + 30
    loading_bar(val)

    ##################### BLACK AND WHITE
    try:
        if useimg:
            gmbrorig = img.open(filename)#.convert("1")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam)#.convert("1")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        rgb_filter = "BW"
        gmbrbw = convert_blackandwhite(gmbrorig)
        limitimg = limit_filter_method(gmbrbw, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = limitimg.resize((320, 240), img.ANTIALIAS)

        image = imgtk.PhotoImage(image=gmbrasli)
        locatebwFilter = tk.Label(image=image)
        locatebwFilter.Image = image
        locatebwFilter.place(x=725, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Limit Proccess -> black&white image, Failed")

    val = val + 30
    loading_bar(val)

    end = datetime.datetime.now()
    elapsed = end - start
    #msgboxshw.showinfo("Time Proccess", "Time elapsed : " + str(elapsed))
    try:
        timeLabel.config(text="Time elapsed = \n" + str(elapsed))
    except Exception as e: 
        print("ERROR =====>> ", e)
        timeLabel = tk.Label(window, text="Time elapsed = \n" + str(elapsed))
        timeLabel.place(x=845,y=15)

    val = val + 10
    loading_bar(val)
    time.sleep(0.5)
    destroy_wndw()

def median_filter_method(source, color_method, minX, minY, maxX, maxY):
    width, height=source.size
    members = [(0,0)] * 9

    ############################## PIL IMAGE
    ## color image = RGB
    ## grayscale image = LA
    ## black and white = 1
    ########################################

    if color_method == "RGB":
        newimg = img.new("RGB",(width,height), "white")
    else:
        newimg = img.new("L",(width,height), "white")
    
    ##### ---------------- kolom // width = lebar
    for i in range(0,maxX+1):
        ##### ------------  baris // height = tinggi
        for j in range(0,maxY+1):
            try:
                members[0] = source.getpixel((i-1,j-1)) #pixel baris 1 kolom 1
            except:
                if color_method == "RGB": members[0] = (0,0,0)
                else: members[0] = 0

            try:
                members[1] = source.getpixel((i-1,j))   #pixel baris 1 kolom 2
            except:
                if color_method == "RGB": members[1] = (0,0,0)
                else: members[1] = 0

            try:
                members[2] = source.getpixel((i-1,j+1)) #pixel baris 1 kolom 3
            except:
                if color_method == "RGB": members[2] = (0,0,0)
                else: members[2] = 0

            try:
                members[3] = source.getpixel((i,j-1))   #pixel baris 2 kolom 1
            except:
                if color_method == "RGB": members[3] = (0,0,0)
                else: members[3] = 0

            members[4] = source.getpixel((i,j))         #pixel baris 2 kolom 2

            try:
                members[5] = source.getpixel((i,j+1))   #pixel baris 2 kolom 3
            except:
                if color_method == "RGB": members[5] = (0,0,0)
                else: members[5] = 0

            try:
                members[6] = source.getpixel((i+1,j-1)) #pixel baris 3 kolom 1
            except:
                if color_method == "RGB": members[6] = (0,0,0)
                else: members[6] = 0

            try:
                members[7] = source.getpixel((i+1,j))   #pixel baris 3 kolom 2
            except:
                if color_method == "RGB": members[7] = (0,0,0)
                else: members[7] = 0

            try:
                members[8] = source.getpixel((i+1,j+1)) #pixel baris 3 kolom 3
            except:
                if color_method == "RGB": members[8] = (0,0,0)
                else: members[8] = 0

            members.sort()
            #print("tuple = " + str(members[4]))
            newimg.putpixel((i,j),(members[4]))

    return newimg

def median_proccess(filename, filecam):
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global timeLabel
    global loading_window
    global progress

    val = 0

    start = datetime.datetime.now()

    #### ----------------------------------------------------- Use OpenCV lib :)
    #medianimgcv = cv.medianBlur(path, 3)
    #b, g, r = cv.split(medianimgcv)
    #gmbr = cv.merge((r, g, b))
    #gmbrcompress = cv.resize(gmbr, (320, 240))
    #gmbrasli = img.fromarray(gmbrcompress)
    
    #### ----------------------------------------------------- Use median method
    try:
        if useimg:
            gmbrorig = img.open(filename).convert("RGB")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam).convert("RGB")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        rgb_filter = "RGB"
        medianimg = median_filter_method(gmbrorig, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = medianimg.resize((320, 240), img.ANTIALIAS)

        imgmediangsc = imgtk.PhotoImage(image=gmbrasli)
        locateFilter = tk.Label(image=imgmediangsc)
        locateFilter.Image = imgmediangsc
        locateFilter.place(x=25, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Median Proccess -> RGB image, Failed")

    val = val + 30
    loading_bar(val)

    #### ----------------------------------------------------- Use OpenCV lib :)
    #cvgsc = cv.cvtColor(path, cv.COLOR_BGR2GRAY)
    #cvgsc = img.open(filename).convert("1")

    #gmbr = cv.medianBlur(cvgsc, 3)
    #gmbrcompress = cv.resize(gmbr, (320, 240))
    #gmbrasli = img.fromarray(gmbrcompress)

    #### ----------------------------------------------------- Use median method
    try:
        if useimg:
            gmbrorig = img.open(filename)#.convert("LA")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam)#.convert("LA")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        #rgb_filter = "GSC"
        gmbrgsc = convert_grayscale(gmbrorig)
        rgb_filter = "RGB"
        medianimg = median_filter_method(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = medianimg.resize((320, 240), img.ANTIALIAS)
        
        image = imgtk.PhotoImage(image=gmbrasli)
        locategscFilter = tk.Label(image=image)
        locategscFilter.Image = image
        locategscFilter.place(x=375, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Median Proccess -> Grayscale image, Failed")

    val = val + 30
    loading_bar(val)
        
    #### ----------------------------------------------------- Use OpenCV lib :)
    #cvgsc = cv.cvtColor(path, cv.COLOR_BGR2GRAY)
    #(_, blackAndWhiteImage) = cv.threshold(cvgsc, 127, 255, cv.THRESH_BINARY)
    #gmbr = cv.medianBlur(blackAndWhiteImage, 3)
    #gmbrcompress = cv.resize(gmbr, (320, 240))
    #gmbrasli = img.fromarray(gmbrcompress)
    
    #### ----------------------------------------------------- Use median method
    try:
        if useimg:
            gmbrorig = img.open(filename)#.convert("1")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam)#.convert("1")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        rgb_filter = "BW"
        gmbrbw = convert_blackandwhite(gmbrorig)
        medianimg = median_filter_method(gmbrbw, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = medianimg.resize((320, 240), img.ANTIALIAS)

        image = imgtk.PhotoImage(image=gmbrasli)
        locatebwFilter = tk.Label(image=image)
        locatebwFilter.Image = image
        locatebwFilter.place(x=725, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Median Proccess -> black&white image, Failed")

    val = val + 30
    loading_bar(val)

    end = datetime.datetime.now()
    elapsed = end - start
    #msgboxshw.showinfo("Time Proccess", "Time elapsed : " + str(elapsed))
    try:
        timeLabel.config(text="Time elapsed = \n" + str(elapsed))
    except Exception as e: 
        print("ERROR =====>> ", e)  
        timeLabel = tk.Label(window, text="Time elapsed = \n" + str(elapsed))
        timeLabel.place(x=845,y=15)

    val = val + 10
    loading_bar(val)
    time.sleep(0.5)
    destroy_wndw()

def another_mean_filter_method(im):
    img = im
    w = 2

    for i in range(2,im.shape[0]-2):
        for j in range(2,im.shape[1]-2):
            block = im[i-w:i+w+1, j-w:j+w+1]
            m = np.mean(block,dtype=np.float32)
            img[i][j] = int(m)
    return img

def mean_filter_method(source, color_method, minX, minY, maxX, maxY):
    width, height=source.size
    members = [(0,0)] * 9

    ############################## PIL IMAGE
    ## color image = RGB
    ## grayscale image = LA
    ## black and white = 1
    ########################################

    if color_method == "RGB":
        newimg = img.new("RGB",(width,height), "white")
    else:
        newimg = img.new("L",(width,height), "white")
    
    ##### ---------------- kolom // width = lebar
    for i in range(0,maxX+1):
        ##### ------------  baris // height = tinggi
        for j in range(0,maxY+1):
            try:
                members[0] = source.getpixel((i-1,j-1)) #pixel baris 1 kolom 1
            except:
                if color_method == "RGB": members[0] = (0,0,0)
                else: members[0] = 0

            try:
                members[1] = source.getpixel((i-1,j))   #pixel baris 1 kolom 2
            except:
                if color_method == "RGB": members[1] = (0,0,0)
                else: members[1] = 0

            try:
                members[2] = source.getpixel((i-1,j+1)) #pixel baris 1 kolom 3
            except:
                if color_method == "RGB": members[2] = (0,0,0)
                else: members[2] = 0

            try:
                members[3] = source.getpixel((i,j-1))   #pixel baris 2 kolom 1
            except:
                if color_method == "RGB": members[3] = (0,0,0)
                else: members[3] = 0

            members[4] = source.getpixel((i,j))         #pixel baris 2 kolom 2

            try:
                members[5] = source.getpixel((i,j+1))   #pixel baris 2 kolom 3
            except:
                if color_method == "RGB": members[5] = (0,0,0)
                else: members[5] = 0

            try:
                members[6] = source.getpixel((i+1,j-1)) #pixel baris 3 kolom 1
            except:
                if color_method == "RGB": members[6] = (0,0,0)
                else: members[6] = 0

            try:
                members[7] = source.getpixel((i+1,j))   #pixel baris 3 kolom 2
            except:
                if color_method == "RGB": members[7] = (0,0,0)
                else: members[7] = 0

            try:
                members[8] = source.getpixel((i+1,j+1)) #pixel baris 3 kolom 3
            except:
                if color_method == "RGB": members[8] = (0,0,0)
                else: members[8] = 0

            #msgboxshw.showinfo("Debug", str(members))
            #print(str(members))
            try:
                sum_val = [sum(x) for x in zip(*members)]
                mean = [y/9 for y in sum_val]
                convert_int = [int(z) for z in mean]
                finalresult = tuple(convert_int)
            except:
                sum_val = sum(members)
                mean = sum_val/9
                finalresult = int(mean)
            #print(str(finalresult))
            newimg.putpixel((i,j),(finalresult))
    return newimg

def mean_process(filename, filecam):
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global timeLabel
    global loading_window
    global progress

    val = 0

    start = datetime.datetime.now()

    ######################## RGB
    try:
        if useimg:
            gmbrorig = img.open(filename).convert("RGB")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam).convert("RGB")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        rgb_filter = "RGB"
        meanimg = mean_filter_method(gmbrorig, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = meanimg.resize((320, 240), img.ANTIALIAS)

        image = imgtk.PhotoImage(image=gmbrasli)
        locateFilter = tk.Label(image=image)
        locateFilter.Image = image
        locateFilter.place(x=25, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Mean Proccess -> RGB image, Failed")

    val = val + 30
    loading_bar(val)

    ####################### GRAYSCALE
    try:
        if useimg:
            gmbrorig = img.open(filename)#.convert("LA")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam)#.convert("LA")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        #rgb_filter = "GSC"
        gmbrgsc = convert_grayscale(gmbrorig)
        rgb_filter = "RGB"
        meanimg = mean_filter_method(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = meanimg.resize((320, 240), img.ANTIALIAS)
        
        image = imgtk.PhotoImage(image=gmbrasli)
        locategscFilter = tk.Label(image=image)
        locategscFilter.Image = image
        locategscFilter.place(x=375, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Mean Proccess -> Grayscale image, Failed")

    val = val + 30
    loading_bar(val)

    ##################### BLACK AND WHITE
    try:
        if useimg:
            gmbrorig = img.open(filename)#.convert("1")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam)#.convert("1")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        rgb_filter = "BW"
        gmbrbw = convert_blackandwhite(gmbrorig)
        meanimg = mean_filter_method(gmbrbw, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = meanimg.resize((320, 240), img.ANTIALIAS)

        image = imgtk.PhotoImage(image=gmbrasli)
        locatebwFilter = tk.Label(image=image)
        locatebwFilter.Image = image
        locatebwFilter.place(x=725, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Mean Proccess -> black&white image, Failed")

    val = val + 30
    loading_bar(val)

    end = datetime.datetime.now()
    elapsed = end - start
    #msgboxshw.showinfo("Time Proccess", "Time elapsed : " + str(elapsed))
    try:
        timeLabel.config(text="Time elapsed = \n" + str(elapsed))
    except Exception as e: 
        print("ERROR =====>> ", e)
        timeLabel = tk.Label(window, text="Time elapsed = \n" + str(elapsed))
        timeLabel.place(x=845,y=15)

    val = val + 10
    loading_bar(val)
    time.sleep(0.5)
    destroy_wndw()

def filter_mode():
    global comboboxfilter
    global filtermode
    global filename
    global filecam
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global loading_window
    global progress

    loading_window = tk.Toplevel()
    loading_window.title("Loading ...")
    loading_window.geometry("300x125")
    loading_window.resizable(width=False, height=False)
    loading_window.bind(lambda e: loading_window.quit())
    load_wndw = tk.Label(loading_window)
    load_wndw.pack()
    loading_window.protocol("WM_DELETE_WINDOW", unclosable)
    progress = Progressbar(loading_window,orient=hrzntl,length=100)
    progress.pack()
    progress["value"]=0
    progress["maximum"]=100

    if(comboboxfilter.get() == filtermode[0]):              ############## FILTER BATAS
        try:
            locateFilter.destroy()
            locategscFilter.destroy()
            locatebwFilter.destroy()
        except: limit_proccess(filename, filecam)
        else: limit_proccess(filename, filecam)
    elif(comboboxfilter.get() == filtermode[1]):            ############## FILTER MEAN
        try:
            locateFilter.destroy()
            locategscFilter.destroy()
            locatebwFilter.destroy()
        except: mean_process(filename, filecam)
        else: mean_process(filename, filecam)
        #msgboxshw.showinfo("Debug", str(filtermode[1]))
    else:                                                   ############## FILTER MEDIAN 
        try:
            locateFilter.destroy()
            locategscFilter.destroy()
            locatebwFilter.destroy()
        except: median_proccess(filename, filecam)
        else: median_proccess(filename, filecam)

def Gaussian(filename, filecam):
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global timeLabel
    global loading_window
    global progress

    val = 0

    start = datetime.datetime.now()

    ######################## RGB
    try:
        if useimg:
            gmbrorig = img.open(filename).convert("RGB")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam).convert("RGB")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        rgb_filter = "RGB"
        gaussiaanimg = convolv.gaussian(gmbrorig, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = gaussiaanimg.resize((320, 240), img.ANTIALIAS)

        image = imgtk.PhotoImage(image=gmbrasli)
        locateFilter = tk.Label(image=image)
        locateFilter.Image = image
        locateFilter.place(x=25, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Gaussian Proccess -> RGB image, Failed")

    val = val + 30
    loading_bar(val)

    ####################### GRAYSCALE
    try:
        if useimg:
            gmbrorig = img.open(filename)#.convert("LA")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam)#.convert("LA")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        #rgb_filter = "GSC"
        gmbrgsc = convert_grayscale(gmbrorig)
        rgb_filter = "RGB"
        gaussiaanimg = convolv.gaussian(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = gaussiaanimg.resize((320, 240), img.ANTIALIAS)
        
        image = imgtk.PhotoImage(image=gmbrasli)
        locategscFilter = tk.Label(image=image)
        locategscFilter.Image = image
        locategscFilter.place(x=375, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Gaussian Proccess -> Grayscale image, Failed")

    val = val + 30
    loading_bar(val)

    ##################### BLACK AND WHITE
    try:
        if useimg:
            gmbrorig = img.open(filename)#.convert("1")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam)#.convert("1")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        rgb_filter = "BW"
        gmbrbw = convert_blackandwhite(gmbrorig)
        gaussiaanimg = convolv.gaussian(gmbrbw, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = gaussiaanimg.resize((320, 240), img.ANTIALIAS)

        image = imgtk.PhotoImage(image=gmbrasli)
        locatebwFilter = tk.Label(image=image)
        locatebwFilter.Image = image
        locatebwFilter.place(x=725, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Gaussian Proccess -> black&white image, Failed")

    val = val + 30
    loading_bar(val)

    end = datetime.datetime.now()
    elapsed = end - start
    #msgboxshw.showinfo("Time Proccess", "Time elapsed : " + str(elapsed))
    try:
        timeLabel.config(text="Time elapsed = \n" + str(elapsed))
    except Exception as e: 
        print("ERROR =====>> ", e)
        timeLabel = tk.Label(window, text="Time elapsed = \n" + str(elapsed))
        timeLabel.place(x=845,y=15)

    val = val + 10
    loading_bar(val)
    time.sleep(0.5)
    destroy_wndw()

def Canny(filename, filecam):
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global timeLabel
    global loading_window
    global progress

    val = 0

    start = datetime.datetime.now()

    ######################## RGB
    try:
        if useimg:
            gmbrorig = img.open(filename).convert("RGB")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam).convert("RGB")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        rgb_filter = "RGB"
        cannyimg = convolv.Canny(gmbrorig, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = cannyimg.resize((320, 240), img.ANTIALIAS)

        image = imgtk.PhotoImage(image=gmbrasli)
        locateFilter = tk.Label(image=image)
        locateFilter.Image = image
        locateFilter.place(x=25, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Canny Proccess -> RGB image, Failed")

    val = val + 30
    loading_bar(val)

    ####################### GRAYSCALE
    try:
        if useimg:
            gmbrorig = img.open(filename)#.convert("LA")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam)#.convert("LA")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        #rgb_filter = "GSC"
        gmbrgsc = convert_grayscale(gmbrorig)
        rgb_filter = "RGB"
        cannyimg = convolv.Canny(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = cannyimg.resize((320, 240), img.ANTIALIAS)
        
        image = imgtk.PhotoImage(image=gmbrasli)
        locategscFilter = tk.Label(image=image)
        locategscFilter.Image = image
        locategscFilter.place(x=375, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Canny Proccess -> Grayscale image, Failed")

    val = val + 30
    loading_bar(val)

    ##################### BLACK AND WHITE
    try: 
        if useimg:
            gmbrorig = img.open(filename)#.convert("1")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam)#.convert("1")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        rgb_filter = "BW"
        gmbrbw = convert_blackandwhite(gmbrorig)
        cannyimg = convolv.Canny(gmbrbw, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = cannyimg.resize((320, 240), img.ANTIALIAS)

        image = imgtk.PhotoImage(image=gmbrasli)
        locatebwFilter = tk.Label(image=image)
        locatebwFilter.Image = image
        locatebwFilter.place(x=725, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Canny Proccess -> black&white image, Failed")

    val = val + 30
    loading_bar(val)

    end = datetime.datetime.now()
    elapsed = end - start
    #msgboxshw.showinfo("Time Proccess", "Time elapsed : " + str(elapsed))
    try:
        timeLabel.config(text="Time elapsed = \n" + str(elapsed))
    except Exception as e: 
        print("ERROR =====>> ", e)
        timeLabel = tk.Label(window, text="Time elapsed = \n" + str(elapsed))
        timeLabel.place(x=845,y=15)

    val = val + 10
    loading_bar(val)
    time.sleep(0.5)
    destroy_wndw()

def Prewitt(filename, filecam):
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global timeLabel
    global loading_window
    global progress

    val = 0

    start = datetime.datetime.now()

    ######################## RGB
    try:
        if useimg:
            gmbrorig = img.open(filename).convert("RGB")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam).convert("RGB")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        rgb_filter = "RGB"
        prewittimg = convolv.prewitt(gmbrorig, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = prewittimg.resize((320, 240), img.ANTIALIAS)

        image = imgtk.PhotoImage(image=gmbrasli)
        locateFilter = tk.Label(image=image)
        locateFilter.Image = image
        locateFilter.place(x=25, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Prewitt Proccess -> RGB image, Failed")

    val = val + 30
    loading_bar(val)

    ####################### GRAYSCALE
    try:
        if useimg:
            gmbrorig = img.open(filename)#.convert("LA")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam)#.convert("LA")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        #rgb_filter = "GSC"
        gmbrgsc = convert_grayscale(gmbrorig)
        rgb_filter = "RGB"
        prewittimg = convolv.prewitt(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = prewittimg.resize((320, 240), img.ANTIALIAS)
        
        image = imgtk.PhotoImage(image=gmbrasli)
        locategscFilter = tk.Label(image=image)
        locategscFilter.Image = image
        locategscFilter.place(x=375, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Prewitt Proccess -> Grayscale image, Failed")

    val = val + 30
    loading_bar(val)

    ##################### BLACK AND WHITE
    try:
        if useimg:
            gmbrorig = img.open(filename)#.convert("1")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam)#.convert("1")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        rgb_filter = "BW"
        gmbrbw = convert_blackandwhite(gmbrorig)
        prewittimg = convolv.prewitt(gmbrbw, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = prewittimg.resize((320, 240), img.ANTIALIAS)

        image = imgtk.PhotoImage(image=gmbrasli)
        locatebwFilter = tk.Label(image=image)
        locatebwFilter.Image = image
        locatebwFilter.place(x=725, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Prewitt Proccess -> black&white image, Failed")

    val = val + 30
    loading_bar(val)

    end = datetime.datetime.now()
    elapsed = end - start
    #msgboxshw.showinfo("Time Proccess", "Time elapsed : " + str(elapsed))
    try:
        timeLabel.config(text="Time elapsed = \n" + str(elapsed))
    except Exception as e: 
        print("ERROR =====>> ", e)
        timeLabel = tk.Label(window, text="Time elapsed = \n" + str(elapsed))
        timeLabel.place(x=845,y=15)

    val = val + 10
    loading_bar(val)
    time.sleep(0.5)
    destroy_wndw()

def Robert(filename, filecam):
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global timeLabel
    global loading_window
    global progress

    val = 0

    start = datetime.datetime.now()

    ######################## RGB
    try:
        if useimg:
            gmbrorig = img.open(filename).convert("RGB")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam).convert("RGB")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        rgb_filter = "RGB"
        robertimg = convolv.robert(gmbrorig, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = robertimg.resize((320, 240), img.ANTIALIAS)

        image = imgtk.PhotoImage(image=gmbrasli)
        locateFilter = tk.Label(image=image)
        locateFilter.Image = image
        locateFilter.place(x=25, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Robert Proccess -> RGB image, Failed")

    val = val + 30
    loading_bar(val)

    ####################### GRAYSCALE
    try: 
        if useimg:
            gmbrorig = img.open(filename)#.convert("LA")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam)#.convert("LA")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        #rgb_filter = "GSC"
        gmbrgsc = convert_grayscale(gmbrorig)
        rgb_filter = "RGB"
        robertimg = convolv.robert(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = robertimg.resize((320, 240), img.ANTIALIAS)
        
        image = imgtk.PhotoImage(image=gmbrasli)
        locategscFilter = tk.Label(image=image)
        locategscFilter.Image = image
        locategscFilter.place(x=375, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Robert Proccess -> Grayscale image, Failed")

    val = val + 30
    loading_bar(val)

    ##################### BLACK AND WHITE
    try: 
        if useimg:
            gmbrorig = img.open(filename)#.convert("1")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
        else:
            gmbrorig = img.open(filecam)#.convert("1")
            minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)
        rgb_filter = "BW"
        gmbrbw = convert_blackandwhite(gmbrorig)
        robertimg = convolv.robert(gmbrbw, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = robertimg.resize((320, 240), img.ANTIALIAS)

        image = imgtk.PhotoImage(image=gmbrasli)
        locatebwFilter = tk.Label(image=image)
        locatebwFilter.Image = image
        locatebwFilter.place(x=725, y=405)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Robert Proccess -> black&white image, Failed")

    val = val + 30
    loading_bar(val)

    end = datetime.datetime.now()
    elapsed = end - start
    #msgboxshw.showinfo("Time Proccess", "Time elapsed : " + str(elapsed))
    try:
        timeLabel.config(text="Time elapsed = \n" + str(elapsed))
    except Exception as e: 
        print("ERROR =====>> ", e)
        timeLabel = tk.Label(window, text="Time elapsed = \n" + str(elapsed))
        timeLabel.place(x=845,y=15)

    val = val + 10
    loading_bar(val)
    time.sleep(0.5)
    destroy_wndw()

def convolution_mode():
    global comboboxconvolution
    global convolutionmode
    global filename
    global filecam
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global loading_window
    global progress

    loading_window = tk.Toplevel()
    loading_window.title("Loading ...")
    loading_window.geometry("300x125")
    loading_window.resizable(width=False, height=False)
    loading_window.bind(lambda e: loading_window.quit())
    load_wndw = tk.Label(loading_window)
    load_wndw.pack()
    loading_window.protocol("WM_DELETE_WINDOW", unclosable)
    progress = Progressbar(loading_window,orient=hrzntl,length=100)
    progress.pack()
    progress["value"]=0
    progress["maximum"]=100

    if(comboboxconvolution.get() == convolutionmode[0]):              ############## Kernel Gaussian
        try:
            locateFilter.destroy()
            locategscFilter.destroy()
            locatebwFilter.destroy()
        except: Gaussian(filename, filecam)#Gaussian
        else: Gaussian(filename, filecam)#Gaussian
    elif(comboboxconvolution.get() == convolutionmode[1]):            ############## Kernel Canny
        try:
            locateFilter.destroy()
            locategscFilter.destroy()
            locatebwFilter.destroy()
        except: Canny(filename, filecam) #Canny
        else: Canny(filename, filecam) #Canny
    elif(comboboxconvolution.get() == convolutionmode[2]):            ############## Kernel Prewitt 
        try:
            locateFilter.destroy()
            locategscFilter.destroy()
            locatebwFilter.destroy()
        except: Prewitt(filename, filecam) #Prewitt
        else: Prewitt(filename, filecam) #Prewitt
    else:                                                             ############## Kernel Robert
        try:
            locateFilter.destroy()
            locategscFilter.destroy()
            locatebwFilter.destroy()
        except: Robert(filename, filecam) #Robert
        else: Robert(filename, filecam) #Robert

def convert_once_filter():
    global filename
    global filecam
    global useimg
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global loading_window
    global progress
    global cnvrtnc2
    global singleconversionfilterbtn
    global timeLabel2

    singleconversionfilterbtn.config(state="disabled")

    val = 0

    loading_window = tk.Toplevel()
    loading_window.title("Loading ...")
    loading_window.geometry("300x125")
    loading_window.resizable(width=False, height=False)
    loading_window.bind(lambda e: loading_window.quit())
    load_wndw = tk.Label(loading_window)
    load_wndw.pack()
    loading_window.protocol("WM_DELETE_WINDOW", unclosable)
    progress = Progressbar(loading_window,orient=hrzntl,length=100)
    progress.pack()
    progress["value"]=0
    progress["maximum"]=100

    cnvrtnc2 = tk.Toplevel()
    cnvrtnc2.withdraw()
    cnvrtnc2.title("Single Conversion")
    cnvrtnc2.geometry("725x345")
    cnvrtnc2.resizable(width=False, height=False)
    cnvrtnc2.protocol("WM_DELETE_WINDOW", unclosable)

    start = datetime.datetime.now()
    
    if useimg:
        gmbrorig = img.open(filename)#.convert("LA")
        minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
    else:
        gmbrorig = img.open(filecam)#.convert("LA")
        minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)

    val = val + 30
    loading_bar(val)

    ############## EXIT #########################
    tk.Button(cnvrtnc2, text="Exit", command=lambda:[cnvrtnc_destroy([True, False, False, False]), cnvrtnc2.destroy()]).place(x=665, y=5)

    ################ ORIGINAL ############################
    gmbrgsc = convert_grayscale(gmbrorig)
    imgresize = gmbrgsc.resize((320, 240), img.ANTIALIAS)
    gmbrtk = imgtk.PhotoImage(image=imgresize)
    tk.Label(cnvrtnc2, text="Original").place(x=25, y=30)
    gmbr = tk.Label(cnvrtnc2, image=gmbrtk)
    gmbr.Image = gmbrtk
    gmbr.place(x=25, y=60)

    val = val + 30
    loading_bar(val)

    if(comboboxfilter.get() == filtermode[0]):              ############## FILTER BATAS
        #rgb_filter = "GSC"
        gmbrgsc = convert_grayscale(gmbrorig)
        rgb_filter = "RGB"
        limitimg = limit_filter_method(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = limitimg.resize((320, 240), img.ANTIALIAS)
        gmbrtk = imgtk.PhotoImage(image=gmbrasli)
        tk.Label(cnvrtnc2, text="Limit").place(x=375, y=30)
        gmbr2 = tk.Label(cnvrtnc2, image=gmbrtk)
        gmbr2.Image = gmbrtk
        gmbr2.place(x=375, y=60)
    elif(comboboxfilter.get() == filtermode[1]):            ############## FILTER MEAN
        #rgb_filter = "GSC"
        gmbrgsc = convert_grayscale(gmbrorig)
        rgb_filter = "RGB"
        meanimg = mean_filter_method(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = meanimg.resize((320, 240), img.ANTIALIAS)
        gmbrtk = imgtk.PhotoImage(image=gmbrasli)
        tk.Label(cnvrtnc2, text="Mean").place(x=375, y=30)
        gmbr2 = tk.Label(cnvrtnc2, image=gmbrtk)
        gmbr2.Image = gmbrtk
        gmbr2.place(x=375, y=60)
    else:                                                   ############## FILTER MEDIAN 
        #rgb_filter = "GSC"
        gmbrgsc = convert_grayscale(gmbrorig)
        rgb_filter = "RGB"
        medianimg = median_filter_method(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = medianimg.resize((320, 240), img.ANTIALIAS)
        gmbrtk = imgtk.PhotoImage(image=gmbrasli)
        tk.Label(cnvrtnc2, text="Median").place(x=375, y=30)
        gmbr2 = tk.Label(cnvrtnc2, image=gmbrtk)
        gmbr2.Image = gmbrtk
        gmbr2.place(x=375, y=60)

    val = val + 40
    loading_bar(val)
    
    end = datetime.datetime.now()
    elapsed = end - start
    #msgboxshw.showinfo("Time Proccess", "Time elapsed : " + str(elapsed))
    try:
        timeLabel2.config(text="Time elapsed = \n" + str(elapsed))
    except Exception as e: 
        print("ERROR =====>> ", e)
        timeLabel2 = tk.Label(cnvrtnc2, text="Time elapsed = \n" + str(elapsed))
        timeLabel2.place(x=525,y=10)

    time.sleep(0.5)
    destroy_wndw()

    cnvrtnc2.update()
    cnvrtnc2.deiconify()

def one_conversion_filter():
    global comboboxfilter
    global filtermode
    global filename
    global filecam
    global useimg
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global loading_window
    global progress
    global cnvrtnc1
    global btnConvertOnceFilter
    global timeLabel1

    btnConvertOnceFilter.config(state="disabled")

    val = 0

    loading_window = tk.Toplevel()
    loading_window.title("Loading ...")
    loading_window.geometry("300x125")
    loading_window.resizable(width=False, height=False)
    loading_window.bind(lambda e: loading_window.quit())
    load_wndw = tk.Label(loading_window)
    load_wndw.pack()
    loading_window.protocol("WM_DELETE_WINDOW", unclosable)
    progress = Progressbar(loading_window,orient=hrzntl,length=100)
    progress.pack()
    progress["value"]=0
    progress["maximum"]=100

    cnvrtnc1 = tk.Toplevel()
    cnvrtnc1.withdraw()
    cnvrtnc1.title("All Filter Conversion")
    cnvrtnc1.geometry("725x595")
    cnvrtnc1.resizable(width=False, height=False)
    cnvrtnc1.protocol("WM_DELETE_WINDOW", unclosable)

    start = datetime.datetime.now()
    
    if useimg:
        gmbrorig = img.open(filename)#.convert("LA")
        minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
    else:
        gmbrorig = img.open(filecam)#.convert("LA")
        minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)

    ############# EXIT #########################
    tk.Button(cnvrtnc1, text="Exit", command=lambda:[cnvrtnc_destroy([False, True, False, False]), cnvrtnc1.destroy()]).place(x=665, y=5)

    ################ ORIGINAL ############################
    gmbrgsc = convert_grayscale(gmbrorig)
    imgresize = gmbrgsc.resize((320, 240), img.ANTIALIAS)
    gmbrtk = imgtk.PhotoImage(image=imgresize)
    tk.Label(cnvrtnc1, text="Original").place(x=25, y=30)
    gmbr = tk.Label(cnvrtnc1, image=gmbrtk)
    gmbr.Image = gmbrtk
    gmbr.place(x=25, y=60)

    val = val + 25
    loading_bar(val)

    ####################### LIMIT ##############################
    #rgb_filter = "GSC"
    gmbrgsc = convert_grayscale(gmbrorig)
    rgb_filter = "RGB"
    limitimg = limit_filter_method(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
    gmbrasli = limitimg.resize((320, 240), img.ANTIALIAS)
    gmbrtk = imgtk.PhotoImage(image=gmbrasli)
    tk.Label(cnvrtnc1, text="Limit").place(x=375, y=30)
    gmbr2 = tk.Label(cnvrtnc1, image=gmbrtk)
    gmbr2.Image = gmbrtk
    gmbr2.place(x=375, y=60)

    val = val + 25
    loading_bar(val)

    ###################### MEDIAN ################################
    #rgb_filter = "GSC"
    gmbrgsc = convert_grayscale(gmbrorig)
    rgb_filter = "RGB"
    medianimg = median_filter_method(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
    gmbrasli = medianimg.resize((320, 240), img.ANTIALIAS)
    gmbrtk = imgtk.PhotoImage(image=gmbrasli)
    tk.Label(cnvrtnc1, text="Median").place(x=25, y=315)
    gmbr3 = tk.Label(cnvrtnc1, image=gmbrtk)
    gmbr3.Image = gmbrtk
    gmbr3.place(x=25, y=345)

    val = val + 25
    loading_bar(val)

    ###################### MEAN ##################################
    #rgb_filter = "GSC"
    gmbrgsc = convert_grayscale(gmbrorig)
    rgb_filter = "RGB"
    meanimg = mean_filter_method(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
    gmbrasli = meanimg.resize((320, 240), img.ANTIALIAS)
    gmbrtk = imgtk.PhotoImage(image=gmbrasli)
    tk.Label(cnvrtnc1, text="Mean").place(x=375, y=315)
    gmbr4 = tk.Label(cnvrtnc1, image=gmbrtk)
    gmbr4.Image = gmbrtk
    gmbr4.place(x=375, y=345)

    val = val + 25
    loading_bar(val)
    
    end = datetime.datetime.now()
    elapsed = end - start
    #msgboxshw.showinfo("Time Proccess", "Time elapsed : " + str(elapsed))
    try:
        timeLabel1.config(text="Time elapsed = \n" + str(elapsed))
    except Exception as e: 
        print("ERROR =====>> ", e)
        timeLabel1 = tk.Label(cnvrtnc1, text="Time elapsed = \n" + str(elapsed))
        timeLabel1.place(x=525,y=10)

    time.sleep(0.5)
    destroy_wndw()

    cnvrtnc1.update()
    cnvrtnc1.deiconify()

def convert_once_convolutional():
    global filename
    global filecam
    global useimg
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global loading_window
    global progress
    global cnvrtnc2
    global singleconversionconvolutionalbtn
    global timeLabel2

    singleconversionconvolutionalbtn.config(state="disabled")

    val = 0

    loading_window = tk.Toplevel()
    loading_window.title("Loading ...")
    loading_window.geometry("300x125")
    loading_window.resizable(width=False, height=False)
    loading_window.bind(lambda e: loading_window.quit())
    load_wndw = tk.Label(loading_window)
    load_wndw.pack()
    loading_window.protocol("WM_DELETE_WINDOW", unclosable)
    progress = Progressbar(loading_window,orient=hrzntl,length=100)
    progress.pack()
    progress["value"]=0
    progress["maximum"]=100

    cnvrtnc2 = tk.Toplevel()
    cnvrtnc2.withdraw()
    cnvrtnc2.title("Single Conversion")
    cnvrtnc2.geometry("725x345")
    cnvrtnc2.resizable(width=False, height=False)
    cnvrtnc2.protocol("WM_DELETE_WINDOW", unclosable)

    start = datetime.datetime.now()
    
    if useimg:
        gmbrorig = img.open(filename)#.convert("LA")
        minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
    else:
        gmbrorig = img.open(filecam)#.convert("LA")
        minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)

    val = val + 30
    loading_bar(val)

    ############## EXIT #########################
    tk.Button(cnvrtnc2, text="Exit", command=lambda:[cnvrtnc_destroy([False, False, True, False]), cnvrtnc2.destroy()]).place(x=665, y=5)

    ################ ORIGINAL ############################
    gmbrgsc = convert_grayscale(gmbrorig)
    imgresize = gmbrgsc.resize((320, 240), img.ANTIALIAS)
    gmbrtk = imgtk.PhotoImage(image=imgresize)
    tk.Label(cnvrtnc2, text="Original").place(x=25, y=30)
    gmbr = tk.Label(cnvrtnc2, image=gmbrtk)
    gmbr.Image = gmbrtk
    gmbr.place(x=25, y=60)

    val = val + 30
    loading_bar(val)

    if(comboboxconvolution.get() == convolutionmode[0]):              ############## Kernel Gaussian
        gmbrgsc = convert_grayscale(gmbrorig)
        rgb_filter = "RGB"
        gaussiaanimg = convolv.gaussian(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = gaussiaanimg.resize((320, 240), img.ANTIALIAS)
        gmbrtk = imgtk.PhotoImage(image=gmbrasli)
        tk.Label(cnvrtnc2, text="Gaussian").place(x=375, y=30)
        gmbr2 = tk.Label(cnvrtnc2, image=gmbrtk)
        gmbr2.Image = gmbrtk
        gmbr2.place(x=375, y=60)
    elif(comboboxconvolution.get() == convolutionmode[1]):            ############## Kernel Canny
        gmbrgsc = convert_grayscale(gmbrorig)
        rgb_filter = "RGB"
        cannyimg = convolv.Canny(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = cannyimg.resize((320, 240), img.ANTIALIAS)
        gmbrtk = imgtk.PhotoImage(image=gmbrasli)
        tk.Label(cnvrtnc2, text="Canny").place(x=375, y=30)
        gmbr2 = tk.Label(cnvrtnc2, image=gmbrtk)
        gmbr2.Image = gmbrtk
        gmbr2.place(x=375, y=60)
    elif(comboboxconvolution.get() == convolutionmode[2]):            ############## Kernel Prewitt 
        gmbrgsc = convert_grayscale(gmbrorig)
        rgb_filter = "RGB"
        prewittimg = convolv.prewitt(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = prewittimg.resize((320, 240), img.ANTIALIAS)
        gmbrtk = imgtk.PhotoImage(image=gmbrasli)
        tk.Label(cnvrtnc2, text="Prewitt").place(x=375, y=30)
        gmbr2 = tk.Label(cnvrtnc2, image=gmbrtk)
        gmbr2.Image = gmbrtk
        gmbr2.place(x=375, y=60)
    else:                                                             ############## Kernel Robert
        gmbrgsc = convert_grayscale(gmbrorig)
        rgb_filter = "RGB"
        robertimg = convolv.robert(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
        gmbrasli = robertimg.resize((320, 240), img.ANTIALIAS)
        gmbrtk = imgtk.PhotoImage(image=gmbrasli)
        tk.Label(cnvrtnc2, text="Robert").place(x=375, y=30)
        gmbr2 = tk.Label(cnvrtnc2, image=gmbrtk)
        gmbr2.Image = gmbrtk
        gmbr2.place(x=375, y=60)

    val = val + 40
    loading_bar(val)
    
    end = datetime.datetime.now()
    elapsed = end - start
    #msgboxshw.showinfo("Time Proccess", "Time elapsed : " + str(elapsed))
    try:
        timeLabel2.config(text="Time elapsed = \n" + str(elapsed))
    except Exception as e: 
        print("ERROR =====>> ", e)
        timeLabel2 = tk.Label(cnvrtnc2, text="Time elapsed = \n" + str(elapsed))
        timeLabel2.place(x=525,y=10)

    time.sleep(0.5)
    destroy_wndw()

    cnvrtnc2.update()
    cnvrtnc2.deiconify()

def one_conversion_convolutional():
    global filename
    global filecam
    global useimg
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global loading_window
    global progress
    global cnvrtnc1
    global btnConvertOnceConvolutional
    global timeLabel1

    btnConvertOnceConvolutional.config(state="disabled")

    val = 0

    loading_window = tk.Toplevel()
    loading_window.title("Loading ...")
    loading_window.geometry("300x125")
    loading_window.resizable(width=False, height=False)
    loading_window.bind(lambda e: loading_window.quit())
    load_wndw = tk.Label(loading_window)
    load_wndw.pack()
    loading_window.protocol("WM_DELETE_WINDOW", unclosable)
    progress = Progressbar(loading_window,orient=hrzntl,length=100)
    progress.pack()
    progress["value"]=0
    progress["maximum"]=100

    cnvrtnc1 = tk.Toplevel()
    cnvrtnc1.withdraw()
    cnvrtnc1.title("All Convolutional Conversion")
    cnvrtnc1.geometry("725x900")
    cnvrtnc1.resizable(width=False, height=False)
    cnvrtnc1.protocol("WM_DELETE_WINDOW", unclosable)

    start = datetime.datetime.now()
    
    if useimg:
        gmbrorig = img.open(filename)#.convert("LA")
        minX, minY, maxX, maxY = getpix.getpixelcoord(filename)
    else:
        gmbrorig = img.open(filecam)#.convert("LA")
        minX, minY, maxX, maxY = getpix.getpixelcoord(filecam)

    ############# EXIT #########################
    tk.Button(cnvrtnc1, text="Exit", command=lambda:[cnvrtnc_destroy([False, False, False, True]), cnvrtnc1.destroy()]).place(x=665, y=5)

    ################ ORIGINAL ############################
    gmbrgsc = convert_grayscale(gmbrorig)
    imgresize = gmbrgsc.resize((320, 240), img.ANTIALIAS)
    gmbrtk = imgtk.PhotoImage(image=imgresize)
    tk.Label(cnvrtnc1, text="Original").place(x=25, y=30)
    gmbr = tk.Label(cnvrtnc1, image=gmbrtk)
    gmbr.Image = gmbrtk
    gmbr.place(x=25, y=60)

    val = val + 20
    loading_bar(val)

    ####################### Gaussian ##############################
    gmbrgsc = convert_grayscale(gmbrorig)
    rgb_filter = "RGB"
    gaussiaanimg = convolv.gaussian(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
    gmbrasli = gaussiaanimg.resize((320, 240), img.ANTIALIAS)
    gmbrtk = imgtk.PhotoImage(image=gmbrasli)
    tk.Label(cnvrtnc1, text="Gaussian").place(x=375, y=30)
    gmbr2 = tk.Label(cnvrtnc1, image=gmbrtk)
    gmbr2.Image = gmbrtk
    gmbr2.place(x=375, y=60)

    val = val + 20
    loading_bar(val)

    ###################### Canny ################################
    gmbrgsc = convert_grayscale(gmbrorig)
    rgb_filter = "RGB"
    cannyimg = convolv.Canny(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
    gmbrasli = cannyimg.resize((320, 240), img.ANTIALIAS)
    gmbrtk = imgtk.PhotoImage(image=gmbrasli)
    tk.Label(cnvrtnc1, text="Canny").place(x=25, y=315)
    gmbr2 = tk.Label(cnvrtnc1, image=gmbrtk)
    gmbr2.Image = gmbrtk
    gmbr2.place(x=25, y=345)

    val = val + 20
    loading_bar(val)

    ###################### Prewitt ################################
    gmbrgsc = convert_grayscale(gmbrorig)
    rgb_filter = "RGB"
    prewittimg = convolv.prewitt(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
    gmbrasli = prewittimg.resize((320, 240), img.ANTIALIAS)
    gmbrtk = imgtk.PhotoImage(image=gmbrasli)
    tk.Label(cnvrtnc1, text="Prewitt").place(x=375, y=315)
    gmbr2 = tk.Label(cnvrtnc1, image=gmbrtk)
    gmbr2.Image = gmbrtk
    gmbr2.place(x=375, y=345)

    val = val + 20
    loading_bar(val)

    ###################### Robert ################################
    gmbrgsc = convert_grayscale(gmbrorig)
    rgb_filter = "RGB"
    robertimg = convolv.robert(gmbrgsc, rgb_filter, minX, minY, maxX, maxY)
    gmbrasli = robertimg.resize((320, 240), img.ANTIALIAS)
    gmbrtk = imgtk.PhotoImage(image=gmbrasli)
    tk.Label(cnvrtnc1, text="Robert").place(x=200, y=600)
    gmbr2 = tk.Label(cnvrtnc1, image=gmbrtk)
    gmbr2.Image = gmbrtk
    gmbr2.place(x=200, y=630)

    val = val + 20
    loading_bar(val)

    end = datetime.datetime.now()
    elapsed = end - start
    #msgboxshw.showinfo("Time Proccess", "Time elapsed : " + str(elapsed))
    try:
        timeLabel1.config(text="Time elapsed = \n" + str(elapsed))
    except Exception as e: 
        print("ERROR =====>> ", e)
        timeLabel1 = tk.Label(cnvrtnc1, text="Time elapsed = \n" + str(elapsed))
        timeLabel1.place(x=525,y=10)

    time.sleep(0.5)
    destroy_wndw()

    cnvrtnc1.update()
    cnvrtnc1.deiconify()

def destroy_additional_button():
    global remove
    global save
    global trackContrast
    global btncontrast
    global trackBrightness
    global btnbrightness
    global btnreset
    global btncombine
    global comboboxlabelgsc
    global comboboxgsc
    global btncomboboxgsc
    global comboboxlabelfilter
    global comboboxfilter
    global btncomboboxfilter
    global timeLabel
    global btnConvertOnceFilter
    global btnConvertOnceConvolutional
    global back
    global comboboxlabelconvolution
    global comboboxconvolution
    global btncomboboxconvolution
    global singleconversionfilterbtn
    global singleconversionconvolutionalbtn
    global btnfilter
    global btnconvolution

    try: btnfilter.destroy()
    except: pass
    try: btnconvolution.destroy()
    except: pass
    try: singleconversionconvolutionalbtn.destroy()
    except: pass
    try: singleconversionfilterbtn.destroy()
    except: pass
    try: comboboxlabelconvolution.destroy()
    except: pass
    try: comboboxconvolution.destroy()
    except: pass
    try: btncomboboxconvolution.destroy()
    except: pass
    try: back.destroy()
    except: pass
    try: remove.destroy()
    except: pass
    try: save.destroy()
    except: pass
    try: trackContrast.destroy()
    except: pass
    try: btncontrast.destroy()
    except: pass
    try: trackBrightness.destroy()
    except: pass
    try: btnbrightness.destroy()
    except: pass
    try: btnreset.destroy()
    except: pass
    try: btncombine.destroy()
    except: pass
    try: comboboxlabelgsc.destroy()
    except: pass
    try: comboboxgsc.destroy()
    except: pass
    try: btncomboboxgsc.destroy()
    except: pass
    try: comboboxlabelfilter.destroy()
    except: pass
    try: comboboxfilter.destroy()
    except: pass
    try: btncomboboxfilter.destroy()
    except: pass
    try: timeLabel.destroy()
    except: pass
    try: btnConvertOnceFilter.destroy()
    except: pass
    try: btnConvertOnceConvolutional.destroy()
    except: pass

def filter_additional_button():
    global btnfilter
    global btnconvolution
    global comboboxlabelfilter
    global comboboxfilter
    global btncomboboxfilter
    global btnConvertOnceFilter
    global back
    global singleconversionfilterbtn

    btnfilter.destroy()
    btnconvolution.destroy()

    ################## BACK BUTTON ##################################
    back = tk.Button(window, text="Back", command=additional_mode)
    back.place(x=570, y=40)

    ################## CONVERT ONCE FILTER #########################
    singleconversionfilterbtn = tk.Button(window, text="Single\nConversion", command=convert_once_filter)
    singleconversionfilterbtn.place(x=570, y=75)

    ############### COMBO BOX FILTER ###########################
    comboboxlabelfilter = tk.Label(window, text="Choose Filter Mode :")
    comboboxlabelfilter.place(x=635, y=10)
    comboboxfilter = ttk.Combobox(window, values=filtermode, width=17)
    comboboxfilter.place(x=645, y=40)
    comboboxfilter.current(0)
    btncomboboxfilter = tk.Button(window, text="Change Filter\nMode", command=filter_mode)
    btncomboboxfilter.place(x=680, y=75)
    btnConvertOnceFilter = tk.Button(window, text="use grayscale image and\nconvert it to all filter", command=one_conversion_filter)
    btnConvertOnceFilter.place(x=805, y=75)

def convolution_additional_button():
    global btnfilter
    global btnconvolution
    global comboboxlabelconvolution
    global comboboxconvolution
    global btncomboboxconvolution
    global back
    global singleconversionconvolutionalbtn
    global btnConvertOnceConvolutional

    btnfilter.destroy()
    btnconvolution.destroy()

    ################## BACK BUTTON ##################################
    back = tk.Button(window, text="Back", command=additional_mode)
    back.place(x=570, y=40)

    ################## CONVERT ONCE CONVOLUTIONAL #########################
    singleconversionconvolutionalbtn = tk.Button(window, text="Single\nConversion", command=convert_once_convolutional)
    singleconversionconvolutionalbtn.place(x=570, y=75)

    ############### COMBO BOX CONVOLUTION ###########################
    comboboxlabelconvolution = tk.Label(window, text="Choose Convolution Mode :")
    comboboxlabelconvolution.place(x=635, y=10)
    comboboxconvolution = ttk.Combobox(window, values=convolutionmode, width=15)
    comboboxconvolution.place(x=645, y=40)
    comboboxconvolution.current(0)
    btncomboboxconvolution = tk.Button(window, text="Change Convolution\nMode", command=convolution_mode)
    btncomboboxconvolution.place(x=680, y=75)
    btnConvertOnceConvolutional = tk.Button(window, text="use grayscale image and\nconvert it to all filter", command=one_conversion_convolutional)
    btnConvertOnceConvolutional.place(x=850, y=75)

def additional_mode():
    global btnfilter
    global btnconvolution
    global comboboxlabelconvolution
    global comboboxconvolution
    global btncomboboxconvolution
    global comboboxlabelfilter
    global comboboxfilter
    global btncomboboxfilter
    global btnConvertOnceFilter
    global btnConvertOnceConvolutional
    global back
    global singleconversionfilterbtn
    global singleconversionconvolutionalbtn
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global timeLabel

    try:
        back.destroy()
        comboboxlabelfilter.destroy()
        comboboxfilter.destroy()
        btncomboboxfilter.destroy()
        singleconversionfilterbtn.destroy()
        btnConvertOnceFilter.destroy()
        locateFilter.destroy()
        locategscFilter.destroy()
        locatebwFilter.destroy()
        timeLabel.destroy()
    except: pass

    try:
        back.destroy()
        comboboxlabelconvolution.destroy()
        comboboxconvolution.destroy()
        btncomboboxconvolution.destroy()
        singleconversionconvolutionalbtn.destroy()
        btnConvertOnceConvolutional.destroy()
        locateFilter.destroy()
        locategscFilter.destroy()
        locatebwFilter.destroy()
        timeLabel.destroy()
    except: pass

    ############### FILTER ##########################
    btnfilter = tk.Button(window, text="Filter Mode", command=filter_additional_button)
    btnfilter.place(x=635, y=5)

    ############### CONVOLUTION #####################
    btnconvolution = tk.Button(window, text="Convolution Mode", command=convolution_additional_button)
    btnconvolution.place(x=635, y=45)

def addtional_button():
    global tab1
    global save
    global trackContrast
    global trackBrightness
    global btncontrast
    global btnbrightness
    global btnreset
    global btncombine
    global grayscaleValue
    global comboboxgsc
    global comboboxfilter
    global filtermode
    global timeLabel
    global comboboxlabelgsc
    global remove
    global btncomboboxgsc
    global comboboxlabelconvolution
    global comboboxconvolution
    global btncomboboxconvolution

    ############ additional button ##################
    ## X = kolom
    ## Y = baris
    
    remove = tk.Button(window, text="reset picture", command=lambda: [clear_img(), destroy_additional_button()])
    remove.place(x=265, y=5)
    save = tk.Button(window, text="Save picture", command=save_img)
    save.place(x=265, y=45)

    additional_mode()

    ############### COMBO BOX GRAYSCALE #######################
    comboboxlabelgsc = tk.Label(window, text="Choose Standart Grayscale Value :")
    comboboxlabelgsc.place(x=385, y=10)
    comboboxgsc = ttk.Combobox(window, values=grayscaleValue, width=15)
    comboboxgsc.place(x=395, y=40)
    comboboxgsc.current(0)
    btncomboboxgsc = tk.Button(window, text="Convert Value", command=convert_value)
    btncomboboxgsc.place(x=395, y=75)

    ############# CONTRAST #####################
    trackContrast = tk.Scale(window, from_=-100, to=100,
                             length=500, orient=hrzntl, command=get_value_contrast)
    trackContrast.place(x=50, y=740)
    btncontrast = tk.Label(window, text="Set Contrast")
    btncontrast.place(x=565, y=760)

    ############# BRIGHTNESS ##################
    trackBrightness = tk.Scale(
        window, from_=-100, to=100, length=500, orient=hrzntl, command=get_value_brightness)
    trackBrightness.place(x=50, y=780)
    btnbrightness = tk.Label(window, text="Set Brightness")
    btnbrightness.place(x=565, y=800)

    ############# RESET ########################
    btnreset = tk.Button(window, text="Reset", command=reset_img_config)
    btnreset.config(state="disabled")
    btnreset.place(x=725, y=760)

    ############# COMBINE ########################
    btncombine = tk.Button(window, text="Contrast + Brightness", command=combine)
    #btncombine.config(state="disabled")
    btncombine.place(x=725, y=800)

def openfile():
    global useimg
    global btncam
    global trackContrast
    global trackBrightness
    useimg = True
    btncam.config(state="disable")
    btnimg.config(state="disable")
    addtional_button()
    process_image()

# Create a new image with the given size
def create_image(i, j):
    image = img.new("RGB", (i, j), "white")
    return image

# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
        return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel

# Create a Grayscale version of the image
def convert_grayscale(image):
    global PAL
    global HDTV
    global HDR
    global Average

    # Get size
    width, height = image.size

    # Create new Image and a Pixel Map
    new = create_image(width, height)
    pixels = new.load()

    # Transform to grayscale
    for i in range(width):
        for j in range(height):
            # Get Pixel
            pixel = get_pixel(image, i, j)

            # Get R, G, B values (This are int from 0 to 255)
            red =   pixel[0]
            green = pixel[1]
            blue =  pixel[2]

            # Transform to grayscale
            if(PAL):
                gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)
            elif(HDTV):
                gray = (red * 0.2126) + (green * 0.7152) + (blue * 0.0722)
            elif(HDR):
                gray = (red * 0.2627) + (green * 0.6780) + (blue * 0.0593)
            else:
                gray = (red * 0.3333) + (green * 0.3334) + (blue * 0.3333)

            # Set Pixel in new image
            pixels[i, j] = (int(gray), int(gray), int(gray))

    # Return new image
    return new

def convert_blackandwhite(image):
    gray = image.convert('L')
    bw = np.asarray(gray).copy()
    bw[bw < 128] = 0    # Black
    bw[bw >= 128] = 255 # White
    bwimg = img.fromarray(bw)
    return bwimg

def process_image():
    # region GLOBAL VARIABLE
    global image
    global locate
    global locategsc
    global gsc
    global imagegsc
    global gmbrgsc
    global gsccompress
    global locatebw
    global useimg
    global usecam
    global gmbr
    global blackAndWhiteImage
    global gmbrcompress
    global gmbrasli
    global image
    global imagebw
    global gmbrbw
    global blackAndWhiteImagecompress
    global update_gmbr
    global update_gsc
    global update_bw
    global path
    global filename
    global filecam
    global gmbrbw
    # endregion

    rgb = None
    gsc_clr = None
    
    try:
        if(useimg):
            filename = dialogbox.askopenfilename(title="Select Image File", filetypes=(
                ("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
            msgboxshw.showinfo("Picutre selected!", filename)
            #path = cv.imread(filename, cv.IMREAD_ANYCOLOR)
            path = img.open(filename)
        else:
            filecam  = "cam_img.jpg"
            #path = cv.imread(filecam, cv.IMREAD_ANYCOLOR)
            path = img.open(filecam)
    except Exception as e: 
        print("ERROR =====>> ", e)
        msgboxshw.showinfo("Program Running Error Occurred", "exit program immediately.")# PATH = " + str(path))
        exitapp()
        
    ############ GAMBAR ASLI GAN ###################
    # Rearrang the color channel
    """
    try:
        b, g, r = cv.split(path)
        rgb = True
    except:
        gryscl = cv.split(path)
        gsc_clr = True
    if(rgb): gmbr = cv.merge((r, g, b))
    else: gmbr = cv.merge((gryscl))
    """
    try:
        gmbr = path.convert("RGB")
        update_gmbr = gmbr
        #gmbrcompress = cv.resize(gmbr, (320, 240))
        #gmbrasli = img.fromarray(gmbrcompress)
        gmbrasli = update_gmbr.resize((320, 240), img.ANTIALIAS)
        image = imgtk.PhotoImage(image=gmbrasli)
        locate = tk.Label(image=image)
        locate.Image = image
        locate.place(x=25, y=130)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("RGB image failed to loaded")

    ############ GAMBAR GRAYSCALE GAN ###################
    ##gsc = cv.cvtColor(path, cv.COLOR_BGR2GRAY)
    #gray_path = img.fromarray(path)
    #gsc = convert_grayscale(gray_path)
    try:
        gsc = convert_grayscale(path)
        update_gsc = gsc
        gsccompress = update_gsc.resize((320, 240), img.ANTIALIAS)
        ##gsccompress = cv.resize(gsc, (320, 240))
        ##gmbrgsc = img.fromarray(gsccompress)
        imagegsc = imgtk.PhotoImage(image=gsccompress)
        locategsc = tk.Label(image=imagegsc)
        locategsc.Image = imagegsc
        locategsc.place(x=375, y=130)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("Grayscale image failed to loaded")

    ############ GAMBAR BW GAN #######################
    try:
        #if(useimg): pathbw = cv.imread(filename, cv.IMREAD_ANYCOLOR)
        #else: pathbw = cv.imread(filecam, cv.IMREAD_ANYCOLOR)
        #gsc_bw = cv.cvtColor(pathbw, cv.COLOR_BGR2GRAY)
        #(_, blackAndWhiteImage) = cv.threshold(gsc_bw, 127, 255, cv.THRESH_BINARY)
        #blackAndWhiteImagecompress = cv.resize(blackAndWhiteImage, (320, 240))
        #gmbrbw = img.fromarray(blackAndWhiteImagecompress)
        blackAndWhiteImage = convert_blackandwhite(path)
        update_bw = blackAndWhiteImage
        bwcompress = update_bw.resize((320, 240), img.ANTIALIAS)
        imagebw = imgtk.PhotoImage(image=bwcompress)
        locatebw = tk.Label(image=imagebw)
        locatebw.Image = imagebw
        locatebw.place(x=725, y=130)
    except Exception as e: 
        print("ERROR =====>> ", e)
        print("black&white image failed to loaded")

def save_img():
    global save
    global useimg
    global usecam
    global update_gmbr
    global update_gsc
    global update_bw
    #save.config(state="disabled")
    save_path = ""
    #if(usecam):
    save_path = dialogbox.asksaveasfilename(title="Save Original Image", filetypes=(
        ("jpeg files", "*.jpg"), ("all files", "*.*")))
    update_gmbr.save(save_path)
    #cv.imwrite(filename=save_path, img=update_gmbr)
    save_path = dialogbox.asksaveasfilename(title="Save GrayScale Image", filetypes=(
        ("jpeg files", "*.jpg"), ("all files", "*.*")))
    update_gsc.save(save_path)
    #cv.imwrite(filename=save_path, img=update_gsc)
    save_path = dialogbox.asksaveasfilename(title="Save BW Image", filetypes=(
        ("jpeg files", "*.jpg"), ("all files", "*.*")))
    update_bw.save(save_path)
    #cv.imwrite(filename=save_path, img=update_bw)
    msgboxshw.showinfo("Picture saved!",
        "Picture saved Succesfully.")
    """
    else:
        save_path = dialogbox.asksaveasfilename(title="Save GrayScale Image", filetypes=(
            ("jpeg files", "*.jpg"), ("all files", "*.*")))
        cv.imwrite(filename=save_path, img=gsc)
        save_path = dialogbox.asksaveasfilename(title="Save BW Image", filetypes=(
            ("jpeg files", "*.jpg"), ("all files", "*.*")))
        cv.imwrite(filename=save_path, img=blackAndWhiteImage)
        msgboxshw.showinfo("Picture saved!",
                           "Picture saved Succesfully.")
    """

def clear_img():
    global locategsc
    global locateFilter
    global locategscFilter
    global locatebwFilter
    global locate
    global locatebw
    global useimg
    global usecam
    global btnimg
    global btncam
    global trackContrast
    global trackBrightness
    global enablereset
    usecam, useimg = False, False
    enablereset = False
    #PAL = True
    #HDTV= False
    #HDR = False
    #Average = False
    btnimg.config(state="normal")
    btncam.config(state="normal")
    #try:(locate.winfo_exists() == 1 and locatebw.winfo_exists() == 1 and locategsc.winfo_exists() == 1):
    try: locate.destroy()
    except: pass
    try: locategsc.destroy()
    except: pass
    try: locatebw.destroy()
    except: pass
    try: locategscFilter.destroy()
    except: pass
    try: locateFilter.destroy()
    except: pass
    try: locatebwFilter.destroy()
    except: pass
        #msgboxshw.showinfo("Program Running Error Occurred", "exit program immediately.")
        #exitapp()
        # locate.config(image="")
        # locategsc.config(image="")
        # locatebw.config(image="")
    trackContrast.config(state="disable")
    trackBrightness.config(state="disable")

def show_frame():
    global frame
    _, frame = cap.read()
    frame = cv.flip(frame, 1)
    cv2image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
    gmbr = img.fromarray(cv2image)
    gmbrtk = imgtk.PhotoImage(image=gmbr)
    cam.gmbrtk = gmbrtk
    cam.configure(image=gmbrtk)
    cam.after(10, show_frame)

def snap_me():
    global frame
    cv.imwrite(filename="cam_img.jpg", img=frame)
    # cap.release()
    cv.waitKey(500)
    cv.destroyAllWindows()
    cam_window.destroy()
    process_image()

def opencam():
    global cam_window
    global cam
    global usecam
    global btnoffcam
    global btnimg
    global tab1
    global save
    global trackContrast
    global trackContrast
    usecam = True
    btncam.config(state="disable")
    btnimg.config(state="disable")
    addtional_button()
    cam_window = tk.Toplevel()
    cam_window.title("senyum dulu dong...")
    cam_window.geometry("750x525")
    cam_window.resizable(width=False, height=False)
    cam_window.bind(lambda e: cam_window.quit())
    cam = tk.Label(cam_window)
    cam.pack()
    show_frame()
    tk.Button(cam_window, text="SNAP ME!", command=snap_me).place(x=330, y=485)
    btnoffcam.config(state="normal")

def offcamcommand():
    global btnoffcam
    global btncam
    btnoffcam.config(state="disabled")
    btncam.config(state="disabled")
    cap.release()
    msgboxshw.showinfo("Webcam shutdown!",
                       "restart the app if you want to use webcam again")

def exitapp():
    global window
    cap.release()
    cv.waitKey(500)
    cv.destroyAllWindows()
    window.destroy()

def setContrast():
    global gmbr
    global gsc
    global blackAndWhiteImage
    global contrastValue
    global gmbrcompress
    global gmbrasli
    global image
    global locategsc
    global locate
    global locatebw
    global imagegsc
    global gmbrgsc
    global gsccompress
    global imagebw
    global gmbrbw
    global blackAndWhiteImagecompress
    global update_gmbr
    global update_gsc
    global update_bw

    ###################### CONTRAST ORIGINAL ###############################
    gmbrcontrast = np.int16(gmbr)
    gmbrcontrast = gmbrcontrast * (contrastValue/100+1) - contrastValue
    gmbrcontrast = np.clip(gmbrcontrast, 0, 255)
    gmbrcontrast = np.uint8(gmbrcontrast)
    update_gmbr = img.fromarray(gmbrcontrast)
    gmbrcompress = update_gmbr.resize((320, 240), img.ANTIALIAS)
    image = imgtk.PhotoImage(image=gmbrcompress)
    locate.config(image=image)

    ###################### CONTRAST GRAYSCALE ##################################
    gmbrcontrastgsc = np.int16(gsc)
    gmbrcontrastgsc = gmbrcontrastgsc * (contrastValue/100+1) - contrastValue
    gmbrcontrastgsc = np.clip(gmbrcontrastgsc, 0, 255)
    gmbrcontrastgsc = np.uint8(gmbrcontrastgsc)
    update_gsc = img.fromarray(gmbrcontrastgsc)
    gsccompress = update_gsc.resize((320, 240), img.ANTIALIAS)
    imagegsc = imgtk.PhotoImage(image=gsccompress)
    locategsc.config(image=imagegsc)

    ###################### CONTRAST BW #################################
    gmbrcontrastbw = np.int16(blackAndWhiteImage)
    gmbrcontrastbw = gmbrcontrastbw * (contrastValue/100+1) - contrastValue
    gmbrcontrastbw = np.clip(gmbrcontrastbw, 0, 255)
    gmbrcontrastbw = np.uint8(gmbrcontrastbw)
    update_bw = img.fromarray(gmbrcontrastbw)
    blackAndWhiteImagecompress = update_bw.resize((320, 240), img.ANTIALIAS)
    imagebw = imgtk.PhotoImage(image=blackAndWhiteImagecompress)
    locatebw.config(image=imagebw)

def get_value_contrast(self):
    global trackContrast
    global btncontrast
    global contrastValue
    global enablereset
    global btnreset
    if(not enablereset):
        btnreset.config(state="normal")
        enablereset = True
    contrastValue = trackContrast.get()
    print(contrastValue)
    strvalue = "Contrast set = " + str(contrastValue)
    btncontrast.config(text=strvalue)
    setContrast()

def setBrightness():
    global gmbr
    global gsc
    global blackAndWhiteImage
    global brightnessValue
    global gmbrcompress
    global gmbrasli
    global image
    global locategsc
    global locate
    global locatebw
    global imagegsc
    global gmbrgsc
    global gsccompress
    global imagebw
    global gmbrbw
    global blackAndWhiteImagecompress
    global update_gmbr
    global update_gsc
    global update_bw

    ################### BRIGHTNESS ORIGINAL #################################
    gmbrbrightness = np.int16(gmbr)
    gmbrbrightness = gmbrbrightness + brightnessValue
    gmbrbrightness = np.clip(gmbrbrightness, 0, 255)
    gmbrbrightness = np.uint8(gmbrbrightness)
    update_gmbr = img.fromarray(gmbrbrightness)
    gmbrcompress = update_gmbr.resize((320, 240), img.ANTIALIAS)
    image = imgtk.PhotoImage(image=gmbrcompress)
    locate.config(image=image)

    ################## BRIGHTNESS GRAYSCALE ###################################
    gmbrgscbrightness = np.int16(gsc)
    gmbrgscbrightness = gmbrgscbrightness + brightnessValue
    gmbrgscbrightness = np.clip(gmbrgscbrightness, 0, 255)
    gmbrgscbrightness = np.uint8(gmbrgscbrightness)
    update_gsc = img.fromarray(gmbrgscbrightness)
    gsccompress = update_gsc.resize((320, 240), img.ANTIALIAS)
    imagegsc = imgtk.PhotoImage(image=gsccompress)
    locategsc.config(image=imagegsc)

    ################ BRIGHTNESS BW ######################################
    gmbrbwbrightness = np.int16(blackAndWhiteImage)
    gmbrbwbrightness = gmbrbwbrightness + brightnessValue
    gmbrbwbrightness = np.clip(gmbrbwbrightness, 0, 255)
    gmbrbwbrightness = np.uint8(gmbrbwbrightness)
    update_bw = img.fromarray(gmbrbwbrightness)
    blackAndWhiteImagecompress = update_bw.resize((320, 240), img.ANTIALIAS)
    imagebw = imgtk.PhotoImage(image=blackAndWhiteImagecompress)
    locatebw.config(image=imagebw)

def get_value_brightness(self):
    global trackBrightness
    global btnbrightness
    global brightnessValue
    global enablereset
    global btnreset
    if(not enablereset):
        btnreset.config(state="normal")
        enablereset = True
    brightnessValue = trackBrightness.get()
    print(brightnessValue)
    strvalue = "Brightness set = " + str(brightnessValue)
    btnbrightness.config(text=strvalue)
    setBrightness()

def reset_img_config():
    """
    global locategsc
    global locate
    global locatebw
    if(locate.winfo_exists() == 1 and locatebw.winfo_exists() == 1 and locategsc.winfo_exists() == 1):
        msgboxshw.showinfo("Debug", "There is Image")
    else:
        msgboxshw.showinfo("Debug", "There is No Image")
    """
    global trackContrast
    global trackBrightness
    trackContrast.set(0)
    trackBrightness.set(0)

def about():
    about_window = tk.Toplevel()
    about_window.withdraw()
    about_window.title("About")
    about_window.geometry("360x110")
    about_window.resizable(width=False, height=False)
    name = tk.Label(about_window, text="Name  :  Andre Arta Kurniawan")
    name.config(anchor="center")
    name.pack()
    nim = tk.Label(about_window, text="NIM  :  16.41020.0016")
    nim.config(anchor="center")
    nim.pack()
    mail =  tk.Label(about_window, text="Reach me at  :  andreartazee@mail.com")
    mail.config(anchor="center")
    mail.pack()
    info =  tk.Label(about_window, text="Dinamika University - Surabaya, East Java, Indonesia")
    info.config(anchor="center")
    info.pack()
    cr = tk.Label(about_window, text="Copyright \u00a9 2019 Penginderaan Elektronika")
    cr.config(anchor="center")
    cr.pack()
    about_window.after(5000, lambda: about_window.destroy())
    about_window.update()
    about_window.deiconify()
    
def main():
    global window
    global btnoffcam
    global btncam
    global btnimg
    global btncontrast
    global trackContrast
    global trackBrightness
    global btnbrightness

    window = tk.Tk()
    window.title("Penginderaan Elektronika")
    try: window.tk.call('wm', 'iconphoto', window._w, imgtk.PhotoImage(file='fav.ico'))
    except: pass
    window.geometry('1075x850')
    window.resizable(width=False, height=False)
    
    #region useless
    # Gets the requested values of the height and widht.
    #windowWidth = window.winfo_reqwidth()
    #windowHeight = window.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    #positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
    #positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)

    ############## TAB CONTROL #####################
    #tabControl = ttk.Notebook(window)                      # Create Tab Control
    #tab1 = ttk.Frame(tabControl)                           # Create a tab 
    #tab2 = ttk.Frame(tabControl)
    #tabControl.add(tab1, text='Image Proccessing')         # Add the tab
    #tabControl.pack(expand=1, fill="both")                 # Pack to make visible

    #labelFrame = tk.LabelFrame(tab1, text="Main Menu")     # Label frame // ----->> GroupBox
    #labelFrame.pack(expand=1, fill="both")                 # Label frame // ----->> GroupBox
    #endregion

    ############# IMAGE ########################
    tk.Label(window, text="Use Image").place(x=10, y=10)
    btnimg = tk.Button(window, text="Open Image", command=openfile)
    btnimg.place(x=110, y=5)
    btnimg.config(state="normal")

    ############# WEBCAM ########################
    tk.Label(window, text="Use Webcam").place(x=10, y=50)
    btncam = tk.Button(window, text="Open Webcam", command=opencam)
    btncam.place(x=110, y=45)
    btncam.config(state="normal")
    btnoffcam = tk.Button(window, text="Turn Off Webcam",
                          command=offcamcommand)
    btnoffcam.place(x=110, y=85)
    btnoffcam.config(state="disabled")

    ############# EXIT #########################
    tk.Button(window, text="Exit App", command=exitapp).place(x=985, y=5)

    ############# ABOUT ########################
    tk.Button(window, text="About", command=about).place(x=1000, y=45)

    window.mainloop()

if __name__ == "__main__":
    main()
