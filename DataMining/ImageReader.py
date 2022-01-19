from PIL import Image

im = Image.open('0016.jpg') # Can be many different formats.
maskIm  = Image.open('0016.bmp') # Can be many different formats.

imageLoader = im.load()
maskImageLoader = maskIm.load()
print(im.size)  # Get the width and hight of the image for iterating over

height = maskIm.size[0] # Get the width and hight of the image for iterating over
width = maskIm.size[1]  # Get the width and hight of the image for iterating over

skin=[[[0]*256]*256]*256
nonSkin=[[[0]*256]*256]*256
skinCount=0
nonSkinCount=0


for i in range(height):
    for j in range(width): 
        print(maskImageLoader[i,j],end="compare to ")
        print(maskImageLoader[i,j])
        if(maskImageLoader[i,j][0]<220&maskImageLoader[i,j][1]<220&maskImageLoader[i,j][2]<220):
            print(imageLoader[i,j])
            skin[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]+=1
            skinCount+=1
        else:
            print(imageLoader[i,j])
            nonSkin[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]+=1
            nonSkinCount+=1

        print("Skin Count: ",skinCount, "Non Skin Count: ", nonSkinCount)     

            