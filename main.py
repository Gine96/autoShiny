from updateshinyfile import update
import pygetwindow as gw
import pyautogui as ag
import time
import sys
from PIL import Image
import json

with open("opzioni.json") as json_data_file:
  data = json.load(json_data_file)

selected = data["game"]
#se cerchi uno starter su smeraldo scegli rubino o zaffiro
starter = eval(data["starter"])
pokettodacercare = data["pokemonDaCercare"] #metti numero del pokemon che vuoi guardando le immagini nelle cartelle

games = {
    "smeraldo":"emerald",
    "rubino":"ruby-sapphire",
    "zaffiro":"ruby-sappire",
    "rossofuoco":"firered-leafgreen",
    "verdefoglia":"firered-leafgreen"
}

winPath = "pokemon\\gen3\\"+games[selected]+("\\back" if starter else "")+"\\shiny\\"
macPath = "pokemon/gen3/"+games[selected]+("/back" if starter else "")+"/shiny/"
shinyPath = winPath if sys.platform == "win32" else macPath

update(selected, games, shinyPath)

shiny = eval(open(games[selected]+"Shiny.txt","r").read())

vbawindow = None

for window in gw.getAllTitles():
  if "VisualBoyAdvance" in window:
    vbawindow = gw.getWindowsWithTitle(window)[0]

#mette focus sulla finestra e la sposta a (0,0)
vbawindow.activate()
vbawindow.moveTo(0,0)

#salva prima
ag.hotkey("shift", "f1")
time.sleep(1)
  
trovato = False
counter = 0
while not trovato:
  counter+=1
  ag.hotkey("f1")
  time.sleep(0.3)

  ag.keyDown("l")
  time.sleep(0.1)
  ag.keyUp("l")
  time.sleep(0.3)
  #entrato nel save
  if selected == "rossofuoco" or selected == "verdefoglia":
    i = 1 if starter else 3
    for x in range(0,i):
      ag.keyDown("l")
      time.sleep(0.2)
      ag.keyUp("l")
      time.sleep(0.2)

  if selected == "smeraldo" or selected == "rubino" or selected == "zaffiro":
    ag.keyDown("l")
    time.sleep(0.1)
    ag.keyUp("l")
    time.sleep(0.3)
    #triggerato il poketto

  if starter:
    if pokettodacercare == "1":
      ag.keyDown("a")
      #DA SISTEMARE
      ag.keyUp("a")
      ag.keyDown("w")
      time.sleep(0.1)
      ag.keyUp("w")

    if pokettodacercare == "7":
      ag.keyDown("a")
      time.sleep(0.1)
      ag.keyUp("a")
      ag.keyDown("w")
      time.sleep(0.1)
      ag.keyUp("w")

    if pokettodacercare == "252":
      ag.keyDown("a")
      time.sleep(0.1)
      ag.keyUp("a")

    if pokettodacercare == "258":
      ag.keyDown("d")
      time.sleep(0.1)
      ag.keyUp("d")

    time.sleep(0.1)
    #andato sulla pokeball giusta
    if selected == "smeraldo" or selected == "rubino" or selected == "zaffiro":
      ag.keyDown("l")
      time.sleep(0.1)
      ag.keyUp("l")
      time.sleep(0.2)
      #scelto pokemon

      ag.keyDown("l")
      time.sleep(0.1)
      ag.keyUp("l")
      time.sleep(0.3)
      #messaggio conferma starter schiacciato
    if selected == "rossofuoco" or selected == "verdefoglia":
      for x in range(0,7):
        ag.keyDown("l")
        time.sleep(0.1)
        ag.keyUp("l")

  while True:
    print(".")
    time.sleep(2)

  ag.keyDown("l")
  time.sleep(0.1)
  ag.keyUp("l")
  ag.keyDown("l")
  time.sleep(0.1)
  ag.keyUp("l")
  #messaggio selvatico schiacciato
  
  time.sleep(0.5)
  screen=[]
  for pixel in ag.screenshot(region=(30,70,200,140)).getdata():
    if pixel not in screen:
      screen.append(pixel)
  count=0
  for item1 in screen:
    for item2 in shiny[pokettodacercare]:
      if item1 == item2:
        count+=1
  print(counter)
  trovato = True if count>len(shiny[pokettodacercare])*0.8 else False

print("Trovato dopo "+str(counter)+" tentativi")