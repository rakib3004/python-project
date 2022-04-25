from PIL import Image

probability=[[[0]*256]*256]*256

f = open("traindatafile.txt", "r")

for i in range (256):
    for j in range (256):
        for k in range (256):
            probability[i][j][k] = float(f.readline())
f.close()


testingImage = Image.open('Testing/Donald.jpg')
testImLoader = testingImage.load()
output_Image = testingImage.load()


for i in range (0, testingImage.size[0]):
    for j in range (0,testingImage.size[1]):
        if probability[testImLoader[i,j][0]][testImLoader[i,j][1]][testImLoader[i,j][2]] >= 1.5:
            output_Image[i,j] = testImLoader[i,j]


            #output_Image[i,j] = (255,255,255)
        else:
            output_Image[i,j] = (255,255,255)
            output_Image[i,j] = (0,0,0)
#testingImage.save("outputImage.bmp")
testingImage.show()