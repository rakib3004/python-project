import glob

import aspose.slides as slides

# Load presentation
imageFile = glob.glob("*.ppt")

for iterator in range(len(imageFile)):

    pptFILE = slides.Presentation(str(imageFile[iterator]))
    convertedFileNameArray = str(imageFile[iterator]).split('.')
    convertedFileName=convertedFileNameArray[0]
    convertedFileName=convertedFileName+".pdf"
    pptFILE.save(convertedFileName, slides.export.SaveFormat.PDF)

#print("Files", iterator, str(imageFile[iterator]))


