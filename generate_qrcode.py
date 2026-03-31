from qrcode import make

link = input('Provide the link: ')

image = make(link)
image.save('qrcode.png')