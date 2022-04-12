import qrcode
# 'https://www.python.org/'
# ' https://sonnytech.netlify.app/'

print("Welcome to My QR Code Generator")
print("Please enter the URL you want to generate a QR Code for")

url = input("Enter the URL: ")

img = qrcode.make(url)
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")

print("Your QR Code has been generated :) ")

