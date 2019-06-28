from PIL import Image
import sys

fil = sys.argv[1]
print(fil)
im = Image.open(fil+".bmp")
im.save(fil+"-600.bmp", dpi=(600,600))