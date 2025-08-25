from PIL import Image

im=Image.open("single-line.png")
w,h=im.size

cropped=im.crop((0,0,w-122,1))

px = list(cropped.getdata())[:841]
resized = Image.new("RGBA", (29, 29))
resized.putdata(px)
resized.save("final-qr.png")