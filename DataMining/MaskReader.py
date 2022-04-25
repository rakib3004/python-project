from PIL import Image
import glob

imageFile = glob.glob("*.jpg")
maskImageFile = glob.glob("*.bmp")

imageFile.sort()
maskImageFile.sort()
skinCount = 0
nonSkinCount = 0
skin = [[[0] * 256] * 256] * 256
nonSkin = [[[0] * 256] * 256] * 256
trainedData = [[[0] * 256] * 256] * 256
probability = [[[0] * 256] * 256] * 256
nonProbability = [[[0] * 256] * 256] * 256
threshHold = [[[0] * 256] * 256] * 256

for iterator in range(len(imageFile) - 1):

    im = Image.open(imageFile[iterator])  # Can be many different formats.
    maskIm = Image.open(maskImageFile[iterator])  # Can be many different formats.

    imageLoader = im.load()
    maskImageLoader = maskIm.load()
    height = maskIm.size[0]  # Get the width and hight of the image for iterating over
    width = maskIm.size[1]  # Get the width and hight of the image for iterating over

    # [get every pixel in height X width]
    for i in range(height):
        for j in range(width):
            # print(maskImageLoader[i,j],end="compare to ")
            # print(maskImageLoader[i,j])
            if (maskImageLoader[i, j][0] < 250 or maskImageLoader[i, j][1] < 250 or maskImageLoader[i, j][2] < 250):
                # print(imageLoader[i,j])
                skin[imageLoader[i, j][0]][imageLoader[i, j][1]][imageLoader[i, j][2]] += 1
                skinCount += 1
            else:
                # print(imageLoader[i,j])
                nonSkin[imageLoader[i, j][0]][imageLoader[i, j][1]][imageLoader[i, j][2]] += 1
                nonSkinCount += 1

    print("Image: ", iterator, "Skin Count: ", skinCount, "Non Skin Count: ", nonSkinCount)
    pointer = 0

    for i in range(height):
        for j in range(width):
            probability[imageLoader[i, j][0]][imageLoader[i, j][1]][imageLoader[i, j][2]] = skinCount and \
                                                                                            skin[imageLoader[i, j][0]][
                                                                                                imageLoader[i, j][1]][
                                                                                                imageLoader[i, j][
                                                                                                    2]] / (skinCount)
    for i in range(height):
        for j in range(width):
            nonProbability[imageLoader[i, j][0]][imageLoader[i, j][1]][imageLoader[i, j][2]] = \
            nonSkin[imageLoader[i, j][0]][imageLoader[i, j][1]][imageLoader[i, j][2]] / (nonSkinCount)
            if (nonProbability[imageLoader[i, j][0]][imageLoader[i, j][1]][imageLoader[i, j][2]] != 0):
                threshHold[imageLoader[i, j][0]][imageLoader[i, j][1]][imageLoader[i, j][2]] = \
                probability[imageLoader[i, j][0]][imageLoader[i, j][1]][imageLoader[i, j][2]] / \
                nonProbability[imageLoader[i, j][0]][imageLoader[i, j][1]][imageLoader[i, j][2]]
                # threshHold[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]=0.45
            else:
                pointer = pointer + 1
                print("Exception", pointer)
                threshHold[imageLoader[i, j][0]][imageLoader[i, j][1]][imageLoader[i, j][2]] = 100

f = open("calcMaskData.txt", "a")

for i in range(256):
    for j in range(256):
        for k in range(256):
            skin[i][j][k] /= skinCount
            nonSkin[i][j][k] /= nonSkinCount
            if (skin[i][j][k] == 0.0 and nonSkin[i][j][k] == 0.0):
                trainedData[i][j][k] = 0
            elif (nonSkin[i][j][k] == 0.0):
                trainedData[i][j][k] = 100
            else:
                trainedData[i][j][k] = nonSkin[i][j][k] and skin[i][j][k] / nonSkin[i][j][k]
            fileValue = str(threshHold[i][j][k])
            f.write(fileValue + "\n")

f.close()

