text = "X-DSPAM-Confidence:    0.8475";
intLen = len(text)
intPoint = text.find('.')
intPoint=intPoint-1
strNumber = text[intPoint:intLen]
floatNumber = float(strNumber)
print(floatNumber)