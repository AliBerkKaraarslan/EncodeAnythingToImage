# encoder.py
# Author: Ali Berk Karaarslan
# Date: 14.07.2024

import re
import binascii
import os
import numpy as np
import sys
import cv2
from PIL import ImageColor

# Encodes The Given File Into An Image.
def encode(sourceFilePath, encodedImagePath):
    print("Encoding Starting...")
    hexCodes = __createHexCodes(sourceFilePath)    
    rgbList =__createRGBCodes(hexCodes)
    imageSize = __calculateEncodedImageSize(rgbList)
    encodedImage = __createEncodedImage(imageSize, imageSize, rgbList)
    path = __saveEncodedImage(encodedImagePath, encodedImage)
    print(f"Encoded Image Saved To: {path}")


# Reads File's Binary Code And Transforms It To Hex Code. Includes File's Extension In The Beginning Of The Hex Code.
def __createHexCodes(sourceFilePath):
    bin_data = bytearray(open(sourceFilePath, 'rb').read())  

    filename, file_extension = os.path.splitext(sourceFilePath)
    extensionInfo = str(len(file_extension)) + file_extension

    bin_data[0:0] = str.encode(extensionInfo)

    hex_data = binascii.hexlify(bin_data)
    hexArray =  (re.sub('(..)', r'\1 ', hex_data.decode('utf-8'))).split()
    hexCodes = []

    for i in range(0,len(hexArray)-2,3):
        hexCodes.append("" + hexArray[i] + hexArray[i+1] + hexArray[i+2])
    
    return hexCodes


# Transforms The Given Hex Codes Lists To Corresponeded RGB Values.
def __createRGBCodes(hexCodes):    
    rgbList = []

    for code in hexCodes:
        rgbList.append(ImageColor.getcolor(f"#{code}", "RGB"))

    return rgbList


# Calculates The Enough Size Of The Image To Store Given RGB List.
def __calculateEncodedImageSize(rgbList):
    imageSize = int(np.sqrt(len(rgbList))) + 1
    return imageSize


# Creates Image Using Given RGB List In Desired Sizes.
def __createEncodedImage(width, height, rgbList):
    image = np.zeros((height,width,3))

    for i in range(len(rgbList)):
        image[(int(i/width))][((i)%width)] = rgbList[i]
    
    return image


# Saves The Given Image To Desired Location.
def __saveEncodedImage(saveLocation, image):
    
    filePath = saveLocation

    if len(os.path.splitext(saveLocation)[1]) != '.png':
        filePath = os.path.splitext(saveLocation)[0] + ".png"

    cv2.imwrite(filePath, image)
    return filePath


# Takes 2 Arguments. Source File Path And Target Encoded Image Path.
if __name__ == "__main__":
    sourceFilePath = sys.argv[1]
    encodedImagePath = sys.argv[2]
    encode(sourceFilePath, encodedImagePath)