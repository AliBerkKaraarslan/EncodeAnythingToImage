# decoder.py
# Author: Ali Berk Karaarslan
# Date: 14.07.2024

import numpy as np
import cv2
import os
import sys

# Decodes The Given Encoded Image.
def decode(encodedImagePath, targetFilePath):
    print("Decoding Starting...")
    rgbValues = __readEncodedImage(encodedImagePath)
    byteArray = __createByteArray(rgbValues)
    fileExtension = __readFileExtension(byteArray)
    byteArrayNew = __removeFileExtensionFromByteArray(byteArray, len(fileExtension))
    filePath = __createFilePath(targetFilePath, fileExtension)
    path = __saveDecodedFile(filePath, byteArrayNew)
    print(f"Decoded Image Saved To: {path}")


# Reads The RGB Values Of The Encoded Image In Given Path And Returns Its RGB Values As List.
def __readEncodedImage(encodedImagePath):
    encodedImage = cv2.imread(encodedImagePath)
    length, _, _ = encodedImage.shape

    rgbValues = []

    for i in range(length):
        for j in range(length):
            rgbValues.append(encodedImage[i][j])

    rgbValuesNP = np.array(rgbValues).astype(np.uint8)

    return rgbValuesNP


# Transforms The Given RGB Values List To Corresponded Byte List.
def __createByteArray(rgbValues):
    byteArray = bytearray()

    for rgb in rgbValues:
        byteArray.append(int(rgb[0]))
        byteArray.append(int(rgb[1]))
        byteArray.append(int(rgb[2]))
    
    return byteArray


# Reads The File Extension From The Byte Array
def __readFileExtension(byteArray):
    extensionSize = int(chr(byteArray[0]))
    extension = str(byteArray[2:extensionSize+1])[12:-2]
    return extension


# Removes The File Extension From Byte Array And Returns Modified Byte Array.
def __removeFileExtensionFromByteArray(byteArray, extensionSize):
    newByteArray = byteArray[extensionSize+2:]
    return newByteArray


# Adds Given File Path If The Given Target File Path Does Not Have One.
def __createFilePath(targetFilePath, fileExtension):
    filePath = targetFilePath
    
    if len(os.path.splitext(targetFilePath)[1]) == 0:
        filePath = filePath + "." + fileExtension
    
    return filePath


# Saves The Decoded File Into The Desired Path.
def __saveDecodedFile(targetFilePath, byteArray):
    with open(targetFilePath, "wb") as file:  
        file.write(byteArray)
    
    return targetFilePath


# Takes Two Arguments. Encoded File's Path And Created Decoded File's Path.
if __name__ == "__main__":
    encodedFilePath = sys.argv[1]
    targetFilePath = sys.argv[2]
    decode(encodedFilePath, targetFilePath)