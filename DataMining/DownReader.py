import numpy as NP
from PIL import Image
import os
from pathlib import Path
 
tc=NP.zeros([256,256,256])
directory= "D:\DBMS2\Mask"
files= Path(directory).glob('*')
cntfile= 10
# for im in os.listdir(directory):
#     cntfile+=1
 
for im2 in files:
    cnt= NP.zeros([256,256,256])
    nskin = NP.zeros([256,256,256])
    proSkin=NP.zeros([256,256,256])
    proNSkin=NP.zeros([256,256,256])
 
    totSkin= 0
    totNon= 0
 
 
    im = Image.open(im2)
 
    for pixel in im.getdata():
        if pixel[0]>200 and pixel[1]>200 and pixel[2]>200:
            cnt[pixel[0]][pixel[1]][pixel[2]]+=1
            totSkin+=1
        else:
            nskin[pixel[0]][pixel[1]][pixel[2]]+=1
            totNon+=1
 
    for pixel in im.getdata():
        proSkin[pixel[0]][pixel[1]][pixel[2]]= cnt[pixel[0]][pixel[1]][pixel[2]]/totSkin
        # print(proSkin[pixel[0]][pixel[1]][pixel[2]])
 
    for pixel in im.getdata():
        proNSkin[pixel[0]][pixel[1]][pixel[2]]= nskin[pixel[0]][pixel[1]][pixel[2]]/totNon
        if proNSkin[pixel[0]][pixel[1]][pixel[2]] != 0:
            tc[pixel[0]][pixel[1]][pixel[2]]+= (proSkin[pixel[0]][pixel[1]][pixel[2]]/proNSkin[pixel[0]][pixel[1]][pixel[2]])/cntfile
        else:
            tc[pixel[0]][pixel[1]][pixel[2]]= 1/cntfile
    im.close()
 
 
 
cnt1= NP.zeros([256,256,256])
nskin1 = NP.zeros([256,256,256])
proSkin1=NP.zeros([256,256,256])
proNSkin1=NP.zeros([256,256,256])
totSkin1= 0
totNon1= 0
 
im1= Image.open('0001.jpg')
wid,hig= im1.size
# print(wid)
# print(hig)
 
for pixel in im1.getdata():
    if pixel[0]<200 and pixel[1]<200 and pixel[2]<200:
        cnt1[pixel[0]][pixel[1]][pixel[2]]+=1
        totSkin1+=1
    else:
        nskin1[pixel[0]][pixel[1]][pixel[2]]+=1
        totNon1+=1
 
o_img = Image.new(mode="RGB", size=im1.size)
pixel_map = o_img.load()
# o_img.show()
 
for pixel in im1.getdata():
    proSkin1[pixel[0]][pixel[1]][pixel[2]]= cnt1[pixel[0]][pixel[1]][pixel[2]]/totSkin1
 
 
    # print(proSkin[pixel[0]][pixel[1]][pixel[2]])
 
for pixel in im1.getdata():
    proNSkin1[pixel[0]][pixel[1]][pixel[2]]= nskin1[pixel[0]][pixel[1]][pixel[2]]/totNon1
 
 
for x in range (0, wid):
    for y in range (0, hig):
        pix = im1.getpixel((x,y))
        if(proNSkin1[pix[0]][pix[1]][pix[2]]<=tc[pix[0]][pix[1]][pix[2]]):
            pixel_map[x,y]=0,0,0
        else:
            pixel_map[x,y]= 255,255,255
# print(cnt)
 
o_img.show()