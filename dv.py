

import random 
import pyxel
#open 
class Jeu:
    def __init__(self):

        pyxel.init(128, 128, title="0.002")


        self.vaisseau_x = 60
        self.vaisseau_y = 60
        self.aste_x = random.randint(1, 129)
        self.aste_y = random.randint(0, 1)
        pyxel.run(self.update, self.draw)

tirs_listeup = []
        
        

    

#deplacement 
def vaisseau_deplacement(self):

        if pyxel.btn(pyxel.KEY_D) and self.vaisseau_x<120:
            self.vaisseau_x += 1
        if pyxel.btn(pyxel.KEY_Q) and self.vaisseau_x>0:
            self.vaisseau_x += -1
        if pyxel.btn(pyxel.KEY_S) and self.vaisseau_y<120:
            self.vaisseau_y += 1
        if pyxel.btn(pyxel.KEY_Z) and self.vaisseau_y>0:
            self.vaisseau_y += -1

def aste_moving(self):
        life = 1
        if life == 1:
         self.aste_y += random.randint(1,2)
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


def update(self):
    global vaisseau_x, vaisseau_y, tirs_listeup 
    tirs_listeup = tirs_creationup(vaisseau_x, vaisseau_y, tirs_listeup)

    tirs_listeup = tirs_deplacementup(tirs_listeup)
        
    self.vaisseau_deplacement()
    self.aste_moving()


def draw(self):

        pyxel.cls(0)
        pyxel.circ(x = self.aste_x, y= self.aste_y, r=3, col=7)
        
        
        pyxel.rect(self.vaisseau_x, self.vaisseau_y, 8, 8, 1)
        pyxel.rect(self.vaisseau_x, self.vaisseau_y, 4, 4, 12)
        pyxel.circb(x= pyxel.mouse_x, y= pyxel.mouse_y, r=1, col=9)
        for tirup in tirs_listeup:
            pyxel.rect(tirup[0], tirup[1], 1, 4, 10)

Jeu()
