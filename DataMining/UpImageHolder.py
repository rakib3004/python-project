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

for iterator in range(len(imageFile)):

    im = Image.open(imageFile[iterator])  # Can be many different formats.
    maskIm = Image.open(maskImageFile[iterator])  # Can be many different formats.

    imageLoader = im.load()
    maskImageLoader = maskIm.load()
    height = maskIm.size[0]  # Get the width and hight of the image for iterating over
    width = maskIm.size[1]  # Get the width and hight of the image for iterating over

    for i in range(height):
        for j in range(width):
            if (maskImageLoader[i, j][0] == 255 and maskImageLoader[i, j][1] == 255 and maskImageLoader[i, j][2] == 255):
                nonSkin[imageLoader[i, j][0]][imageLoader[i, j][1]][imageLoader[i, j][2]] += 1
                nonSkinCount += 1
            else:
                skin[imageLoader[i, j][0]][imageLoader[i, j][1]][imageLoader[i, j][2]] += 1
                skinCount += 1

    print("Image: ", iterator, "Skin Count: ", skinCount, "Non Skin Count: ", nonSkinCount)
    pointer = 0

f = open("traindatafile.txt", "w")
for i in range(0, 256):
    for j in range(0, 256):
        for k in range(0, 256):
            probability[i][j][k] = skin[i][j][k] / skinCount
            nonProbability[i][j][k] = nonSkin[i][j][k] / nonSkinCount
            if nonProbability[i][j][k] == 0 and probability[i][j][k] == 0:
                probability[i][j][k] = 0
            elif nonProbability[i][j][k] == 0:
                probability[i][j][k] = 100
            else:
                probability[i][j][k] = probability[i][j][k] / nonProbability[i][j][k]

            f.write(str(probability[i][j][k]) + "\n")
f.close()





