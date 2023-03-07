from PIL import Image
from PIL.ExifTags import TAGS
from contextlib import closing
import os

print("v2303071")
in_path = input("Directory: ")
in_percentage = int(input("% resize: "))
files = os.listdir(in_path)

for file in files:
    base, ext = os.path.splitext(file)
    if ext == ".jpg" or ext == ".jpeg":
        with closing(Image.open(os.path.join(in_path, file))) as im:
            exif_data = im.getexif()
            if exif_data:
                exif = {
                    TAGS[k]: v
                    for k, v in im._getexif().items()
                    if k in TAGS
                }
            else: exif = {}
            orientation = exif.get('Orientation', 1)
            if orientation == 3:
                im = im.rotate(180, expand=True)
            elif orientation == 6:
                im = im.rotate(270, expand=True)
            elif orientation == 8:
                im = im.rotate(90, expand=True)
            im.save(os.path.join(in_path, file), quality = in_percentage)

print("Done!")
