from PIL import Image

threshHold=[[[0.0]*256]*256]*256

f = open("calcData.txt", "r")


# data to 3*3 matrix
i=0
j=0
k=0
for data in f:
    if(k==256):
        j=j+1
        if(j==256):
            i=i+1
    threshHold[i%256][j%256][k%256]=float(data)
    k=k+1




skin2 = [[[0] * 256] * 256] * 256
nonSkin2 = [[[0] * 256] * 256] * 256
skin2Count = 0
nonSkin2Count = 0
probability2 = [[[0] * 256] * 256] * 256
nonProbability2 = [[[0] * 256] * 256] * 256

testingImage = Image.open('Testing/Donald.jpg')

for pixel in testingImage.getdata():
    if pixel[0] < 200 and pixel[1] < 200 and pixel[2] < 200:
        skin2[pixel[0]][pixel[1]][pixel[2]] += 1
        skin2Count += 1
    else:
        nonSkin2[pixel[0]][pixel[1]][pixel[2]] += 1
        nonSkin2Count += 1

o_img = Image.new(mode="RGB", size=testingImage.size)
imageLoader_map = o_img.load()
# o_img.show()

for imageLoader in testingImage.getdata():
    probability2[imageLoader[0]][imageLoader[1]][imageLoader[2]] = skin2[imageLoader[0]][imageLoader[1]][
                                                                       imageLoader[2]] / skin2Count

    # print(proSkin[imageLoader[0]][imageLoader[1]][imageLoader[2]])

for imageLoader in testingImage.getdata():
    nonProbability2[imageLoader[0]][imageLoader[1]][imageLoader[2]] = nonSkin2[imageLoader[0]][imageLoader[1]][
                                                                          imageLoader[2]] / nonSkin2Count

for x in range(testingImage.size[0]):
    for y in range(testingImage.size[1]):
        pix = testingImage.getpixel((x, y))
        if (threshHold[pix[0]][pix[1]][pix[2]] < 1):
            imageLoader_map[x, y] = 0,0,0
        else:
            imageLoader_map[x, y] = 255, 255, 255
# print(cnt)

o_img.show()

# for tImage in testingImage:
# tImage