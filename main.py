from PIL import Image
import collections
import os
import sys

games = ["emerald","ruby-sapphire","firered-leafgreen"]

winPath = "pokemon\\gen3\\"+games[0]+"\\shiny\\"
macPath = "pokemon/gen3/"+games[0]+"/shiny/"

shinyPath = winPath if sys.platform == "win32" else macPath

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

#prova

f = open(games[0]+"Shiny.txt","w")
f.write(str(images))
f.close()

#controlla che due liste contengano gli stessi colori
#print(collections.Counter(oneColors) == collections.Counter(twoColors))
