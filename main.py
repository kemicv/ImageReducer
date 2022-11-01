from PIL import Image
import os

in_path = input("Directory: ")
in_percentage = int(input("% resize: ")) / 100

files = os.listdir(in_path)

for file in files:
    if file[-4:] == ".jpg":
        with Image.open(os.path.join(in_path, file)) as im:

            new_size = (int(im.width * in_percentage),
                        int(im.height * in_percentage))
            im = im.resize(new_size)

            im.save(os.path.join(in_path,file))

print("Done!")
