import re

iEmailText = "From: bsse1129@iit.du.ac.bd 4 Dec 16 08:14:26"
iList = iEmailText.split()
iEmail = iList[1]
iID = iEmail.split('@')
print("Here, your organization name :", iID[1])