import pyxel

class Jeu:
    def __init__(self):

        # taille de la fenetre 128x128 pixels
        # ne pas modifier
        pyxel.init(128, 128, title="Nuit du c0de")

        # position initiale du vaisseau
        # (origine des positions : coin haut gauche)
        self.vaisseau_x = 60
        self.vaisseau_y = 60

        # initialisation des tirs
        self.tirs_liste = []

        pyxel.run(self.update, self.draw)


    def vaisseau_deplacement(self):

        if pyxel.btn(pyxel.KEY_RIGHT) and self.vaisseau_x<120:
            self.vaisseau_x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.vaisseau_x>0:
            self.vaisseau_x += -1
        if pyxel.btn(pyxel.KEY_DOWN) and self.vaisseau_y<120:
            self.vaisseau_y += 1
        if pyxel.btn(pyxel.KEY_UP) and self.vaisseau_y>0:
            self.vaisseau_y += -1


    def tirs_creation(self):

        if pyxel.btnr(pyxel.KEY_SPACE):
            self.tirs_liste.append([self.mousse-x+4, self.mousse_y-4])


    def tirs_deplacement(self):

        for tir in  self.tirs_liste:
            tir[1] -= 1
            if  tir[1]<-8:
                self.tirs_liste.remove(tir)


    def update(self):

        self.vaisseau_deplacement()
        self.tirs_creation()
        self.tirs_deplacement()

    def draw(self):

        # vide la fenetre
        pyxel.cls(0)

        # vaisseau (carre 8x8)
        pyxel.rect(self.vaisseau_x, self.vaisseau_y, 8, 8, 1)

        # tirs
        for tir in self.tirs_liste:
            pyxel.rect(tir[0], tir[1], 1, 4, 10)
