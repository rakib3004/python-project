import urllib.request, urllib.parse, urllib.error

iHtmlFile = urllib.request.urlopen('https://rakib3004.github.io/index.html')

for iGetContent in iHtmlFile:
    print(iGetContent.decode().strip())