import pyxel
import random

pyxel.init(128, 128, title="Nuit du c0de")

vaisseau_x = 60
vaisseau_y = 60


tirs_listeup = []



def vaisseau_deplacement(x, y):

    if pyxel.btn(pyxel.KEY_D):
        if (x < 120) :
            x = x + 2
    if pyxel.btn(pyxel.KEY_Q):
        if (x > 0) :
            x = x - 2
    if pyxel.btn(pyxel.KEY_S):
        if (y < 120) :
            y = y + 2
    if pyxel.btn(pyxel.KEY_Z):
        if (y > 0) :
            y = y - 2
    return x, y



        

def tirs_creationup(x, y, tirs_listeup):

    if pyxel.btnr(pyxel.KEY_SPACE):
        tirs_listeup.append([x+4, y-4])
    return tirs_listeup

def tirs_deplacementup(tirs_listeup):

    for tirup in tirs_listeup:
        tirup[1] -= 4  
        if  tirup[1]<-8:
            tirs_listeup.remove(tirup)
    return tirs_listeup

    

def update():
   
    global vaisseau_x, vaisseau_y, tirs_listeup 

    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)

    tirs_listeup = tirs_creationup(vaisseau_x, vaisseau_y, tirs_listeup)

    tirs_listeup = tirs_deplacementup(tirs_listeup)






def draw():

    pyxel.cls(0)
    pyxel.circb(x= pyxel.mouse_x, y= pyxel.mouse_y, r=1, col=9)
    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

    for tirup in tirs_listeup:
        pyxel.rect(tirup[0], tirup[1], 1, 4, 10)

pyxel.run(update, draw)
