from PIL import Image
import glob

imageFile = glob.glob("*91.jpg")
maskImageFile = glob.glob("*91.bmp")

imageFile.sort()
maskImageFile.sort()
skinCount=0
nonSkinCount=0
skin=[[[0]*256]*256]*256
nonSkin=[[[0]*256]*256]*256
trainedData=[[[0]*256]*256]*256
probability=[[[0]*256]*256]*256
nonProbability=[[[0]*256]*256]*256
threshHold=[[[0]*256]*256]*256

for iterator in range(len(imageFile)):

    im = Image.open(imageFile[iterator]) # Can be many different formats.
    maskIm  = Image.open(maskImageFile[iterator]) # Can be many different formats.

    imageLoader = im.load()
    maskImageLoader = maskIm.load()
    height = maskIm.size[0] # Get the width and hight of the image for iterating over
    width = maskIm.size[1]  # Get the width and hight of the image for iterating over

    



    for i in range(height):
        for j in range(width): 
            #print(maskImageLoader[i,j],end="compare to ")
            #print(maskImageLoader[i,j])
            if(imageLoader[i,j][0]<200&imageLoader[i,j][1]<200&imageLoader[i,j][2]<200):
                #print(imageLoader[i,j])
                skin[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]+=1
                skinCount+=1
            else:
                #print(imageLoader[i,j])
                nonSkin[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]+=1
                nonSkinCount+=1

    print("Image: ",iterator,"Skin Count: ",skinCount, "Non Skin Count: ", nonSkinCount)     

    for i in range(height):
        for j in range(width): 
            probability[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]= skin[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]/(skinCount)
    for i in range(height):
        for j in range(width): 
            nonProbability[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]= nonSkin[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]/(nonSkinCount)
            if(nonProbability[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]!=0):
                threshHold[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]+=probability[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]/nonProbability[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]
            else:
                threshHold[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]=1/len(imageFile)


for i in range(256):
    for j in range(256):
        for k in range (256):
            skin[i][j][k]/=skinCount
            nonSkin[i][j][k]/=nonSkinCount
            if(skin[i][j][k]==0.0 and nonSkin[i][j][k]==0.0):
                trainedData[i][j][k]=0
            elif(nonSkin[i][j][k]==0.0):
                trainedData[i][j][k]=100
            else:
                trainedData[i][j][k]= nonSkin[i][j][k] and skin[i][j][k]/nonSkin[i][j][k]


skin2=[[[0]*256]*256]*256
nonSkin2=[[[0]*256]*256]*256
skin2Count=0
nonSkin2Count=0
probability2=[[[0]*256]*256]*256
nonProbability2=[[[0]*256]*256]*256


testingImage = Image.open('out.jpg')

for pixel in testingImage.getdata():
    if pixel[0]<200 and pixel[1]<200 and pixel[2]<200:
        skin2[pixel[0]][pixel[1]][pixel[2]]+=1
        skin2Count+=1
    else:
        nonSkin2[pixel[0]][pixel[1]][pixel[2]]+=1
        nonSkin2Count+=1

o_img = Image.new(mode="RGB", size=testingImage.size)
imageLoader_map = o_img.load()
# o_img.show()

for imageLoader in testingImage.getdata():
    probability2[imageLoader[0]][imageLoader[1]][imageLoader[2]]= skin2[imageLoader[0]][imageLoader[1]][imageLoader[2]]/skin2Count
        

    # print(proSkin[imageLoader[0]][imageLoader[1]][imageLoader[2]])

for imageLoader in testingImage.getdata():
    nonProbability2[imageLoader[0]][imageLoader[1]][imageLoader[2]]= nonSkin2[imageLoader[0]][imageLoader[1]][imageLoader[2]]/nonSkin2Count


for x in range (testingImage.size[0]):
    for y in range (testingImage.size[1]):
        pix = testingImage.getpixel((x,y))
        if(probability2[pix[0]][pix[1]][pix[2]]<=threshHold[pix[0]][pix[1]][pix[2]]):
            imageLoader_map[x,y]=0,0,0
        else:
            imageLoader_map[x,y]= 255,255,255
# print(cnt)

o_img.show()

#for tImage in testingImage:
    #tImage