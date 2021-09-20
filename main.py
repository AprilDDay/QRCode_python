#https://pypi.org/project/qrcode/

import qrcode 
img = qrcode.make("https://www.youtube.com")
img.save("youtubeQR.jpg")

#https://www.analyticsvidhya.com/blog/2021/07/3-interesting-python-projects-with-code-for-beginners/