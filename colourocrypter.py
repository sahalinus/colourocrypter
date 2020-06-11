import math, os, sys, base64
from PIL import Image, ImageDraw

# "Colourcrypter" by Sahalinus
# GitHub:   https://github.com/sahalinus
# Telegram: https://t.me/hat_kid

def encrypt(): # Encryption
    path = input("\nEnter path of file to Encrypt: ")
    if (path[-1:] == "\'" and path[:1] == "\'") or (path[-1:] == "\"" and path[:1] == "\""): path = path[1:-1]
    f = open(path, "rb")
    file = f.read()
    f.close()
    
    l = []
    for i in base64.b64encode(file): l.append(i)
    l.append(1)
    for i in base64.b64encode(str.encode(os.path.basename(path))): l.append(i)
    
    if (len(l) % 3) != 0: l.append(0)
    if (len(l) % 3) != 0: l.append(0)
    
    wh = math.ceil(math.sqrt(math.ceil(len(l)/3)))
    image = Image.new("RGB", (wh, wh))
    draw = ImageDraw.Draw(image)
    
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if len(l) > 0:
                r = l.pop()
                g = l.pop()
                b = l.pop()
            else:
                r, g, b = 0, 0, 0
            draw.point((x, y), (r*2, g*2, b*2))
    
    image.save("result.png", "PNG") # Saving encrypted image to "./result.png"
    print("\nSuccess! File \"result.png\" was Encrypted are saved!")

def decrypt(): # Decryption
    path = input("\nEnter path of file to Decrypt: ")
    if (path[-1:] == "\'" and path[:1] == "\'") or (path[-1:] == "\"" and path[:1] == "\""): path = path[1:-1]
    
    l = []
    
    try:
        image = Image.open(path)
        pix = image.load()
    except:
        print("Error...")
        return
    
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            l.append(pix[x, y][0])
            l.append(pix[x, y][1])
            l.append(pix[x, y][2])
    
    l.reverse()
    l = [i for i in l if i != 0]
    
    a, name = [], []
    c = 0
    
    for i in l:
        i = int(i / 2)
        if i == 1:
            c = 1
            continue
        if c == 0:
            a.append(i)
        else:
            name.append(i)
    
    l = base64.b64decode(str.encode("".join(map(chr, list(a)))))
    name = base64.b64decode(str.encode("".join(map(chr, name)))).decode("utf-8")
    
    f = open("result-" + name, "wb")
    f.write(l) # Saving decrypted file to "./name-filename.ext"
    f.close()
    print("\nSuccess! File \"result-"+name+"\" was Decrypted and are Saved.")

try:
    print("\nWelcome to \"Colourcrypter\"!")
    print("by Sahalinus (t.me/hat_kid)\n")
    print("1: Encrypt file to PNG image\n2: Decrypt encrypted PNG image\n")
    choice = input(">: ")
except:
	print("\n\nBye.")
	sys.exit()

if(choice == "1"): encrypt()
elif(choice == "2"): decrypt()
else: print("\nIncorrected choice.")
