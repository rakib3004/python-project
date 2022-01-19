from PIL import Image

im = Image.open('0000.jpg') # Can be many different formats.
maskIm  = Image.open('0000.bmp') # Can be many different formats.

imageLoader = im.load()
maskImageLoader = maskIm.load()
print(im.size)  # Get the width and hight of the image for iterating over

height = maskIm.size[0] # Get the width and hight of the image for iterating over
width = maskIm.size[1]  # Get the width and hight of the image for iterating over

skin=[[[0]*256]*256]*256
nonSkin=[[[0]*256]*256]*256
trainedData=[[[0]*256]*256]*256

skinCount=0
nonSkinCount=0


for i in range(height):
    for j in range(width): 
        print(maskImageLoader[i,j],end="compare to ")
        print(maskImageLoader[i,j])
        if(imageLoader[i,j][0]<255&imageLoader[i,j][1]<255&imageLoader[i,j][2]<255):
            print(imageLoader[i,j])
            skin[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]+=1
            skinCount+=1
        else:
            print(imageLoader[i,j])
            nonSkin[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]+=1
            nonSkinCount+=1

        print("Skin Count: ",skinCount, "Non Skin Count: ", nonSkinCount)     


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

for i in range(256):
    for j in range(256):
        for k in range (256):
            print((i,j,k),float(trainedData[i][j][k]))


