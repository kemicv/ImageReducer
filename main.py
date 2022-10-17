from PIL import Image
import os, sys

resize_percentajes = {
    "25%": 4,
    "50%": 2
}

if len(sys.argv) != 3:
    if sys.argv[1] in resize_percentajes:
        percentaje_value = resize_percentajes[sys.argv[1]]

        currentPath = os.getcwd()
        files = os.listdir(currentPath)

        for file in files:

            if file[-4:] == ".jpg":
                with Image.open(file) as im:
                    im = im.resize((im.width//percentaje_value,
                                    im.height//percentaje_value))
                    im.save(file)

        print("Done!")

    else: print("Invalid argument, try introducing 25% or 50%")
else: print("Invalid argument")
