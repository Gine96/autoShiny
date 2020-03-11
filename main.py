from PIL import Image
import collections
import os

shinyPath = "pokemon/gen3/ruby-sapphire/shiny/"

filenames = []

for r, d, f in os.walk(shinyPath):
  for file in f:
    if ".png" in file:
      filenames.append(file)

images = {}
imagesT = {}
for name in filenames:
  imagesT[name[:-4]] = Image.open(shinyPath+name).convert("RGB")

for name in filenames:
  imgColors = []
  for pixel in imagesT[name[:-4]].getdata():
    if pixel not in imgColors:
      imgColors.append(pixel)
  images[name[:-4]]=imgColors

f = open("rsShiny.txt","w")
f.write(str(images))
f.close()

#controlla che due liste contengano gli stessi colori
#print(collections.Counter(oneColors) == collections.Counter(twoColors))
