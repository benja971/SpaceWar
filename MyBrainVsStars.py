import pygame, json, os
# from tkinter import *
from random import randint, random
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

pygame.init()

largeur, hauteur = 1920, 1080
fenetre = pygame.display.set_mode((largeur,hauteur), flags = pygame.FULLSCREEN)


def getImgBank(path: str) -> dict:
	"""Return a dict containing all images in a folder with recursion."""
	d = {}
	for f in os.listdir(path):
		if len(f) > 4 and f[-4:] in ('.png', '.jpg'):
			d[f[:-4]] = pygame.image.load(f'{path}/{f}').convert_alpha()
		else:
			d[f] = getImgBank(f'{path}/{f}')
	return d

bank = getImgBank("images/Space")

class ElementGraphique():
	# Le constructeur basique
	def __init__(self, img, x, y):
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y 

	def Afficher(self, window) :
		window.blit(self.image, self.rect)


class Perso(ElementGraphique):
	def __init__(self, img, x, y):
		super(Perso, self).__init__(img, x, y)
		self.vie = 1
		self.vitesse = 5
		self.angle = 0
		self.anglemax = 0

	def Deplacer(self, touches, largeur, hauteur):
		if touches[pygame.K_d] and self.rect.x <= largeur-self.rect.w:
			self.rect.x += self.vitesse
		if touches[pygame.K_a] and self.rect.x >= 0:
			self.rect.x -= self.vitesse
		if touches[pygame.K_w] and self.rect.y >= 0:
			self.rect.y -= self.vitesse
		if touches[pygame.K_s] and self.rect.y <= hauteur-self.rect.h:
			self.rect.y += self.vitesse

	def Orientation(self,N,S,E,W,NE,NW,SE,SW):
		print(self.anglemax, self.angle, end = '\r')	

		if N:
			if 46<=self.angle<=180:
				self.anglemax = 0

			elif 180<self.angle<=316:
				self.anglemax = 360

			if self.angle < self.anglemax:
				self.angle+=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)

			elif self.angle > self.anglemax:
				self.angle-=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)
			
			elif self.angle == self.anglemax:
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)


		if S:
			self.anglemax = 180

			if self.angle < self.anglemax:
				self.angle+=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)

			elif self.angle > self.anglemax:
				self.angle-=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)
			
		
			elif self.angle == self.anglemax:
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)

		if E:
			if self.angle == 360:
				self.angle = 0

			self.anglemax = 90

			if self.angle < self.anglemax:
				self.angle+=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)

			elif self.angle > self.anglemax:
				self.angle-=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)
			
			elif self.angle == self.anglemax:
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)


		if W:
			if self.angle == 0:
				self.angle = 360
				
			self.anglemax = 270

			if self.angle < self.anglemax:
				self.angle+=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)

			elif self.angle > self.anglemax:
				self.angle-=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)
			
			elif self.angle == self.anglemax:
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)


		if NW:
			if self.angle == 0:
				self.angle = 360
			self.anglemax = 316

			if self.angle < self.anglemax:
				self.angle+=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)

			elif self.angle > self.anglemax:
				self.angle-=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)
			
			elif self.angle == self.anglemax:
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)

		if NE:
			self.anglemax = 46

			if self.angle < self.anglemax:
				self.angle+=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)

			elif self.angle > self.anglemax:
				self.angle-=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)
			
			elif self.angle == self.anglemax:
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)


		if SE:
			self.anglemax = 136

			if self.angle < self.anglemax:
				self.angle+=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)

			elif self.angle > self.anglemax:
				self.angle-=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)
			
			elif self.angle == self.anglemax:
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)

		if SW:
			self.anglemax = 226

			if self.angle < self.anglemax:
				self.angle+=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)

			elif self.angle > self.anglemax:
				self.angle-=2
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)
			
			elif self.angle == self.anglemax:
				fenetre.blit(pygame.transform.rotate(bank["tile000"], -self.angle), self.rect)
		

	def Direction(self, touches, N,S,E,W,NE,NW,SE,SW):
		if touches[pygame.K_d]: #E
			N,S,E,W,NE,NW,SE,SW = False,False,True,False,False,False,False,False
			
		if touches[pygame.K_a]: #W
			N,S,E,W,NE,NW,SE,SW = False,False,False,True,False,False,False,False

		if touches[pygame.K_w]: #N
			N,S,E,W,NE,NW,SE,SW = True,False,False,False,False,False,False,False
			
		if touches[pygame.K_s]: #S
			N,S,E,W,NE,NW,SE,SW = False,True,False,False,False,False,False,False
				
		if touches[pygame.K_w] and touches[pygame.K_a]: #NW
			N,S,E,W,NE,NW,SE,SW = False,False,False,False,False,True,False,False
			
		if touches[pygame.K_w] and touches[pygame.K_d]: #NE
			N,S,E,W,NE,NW,SE,SW = False,False,False,False,True,False,False,False

		if touches[pygame.K_s] and touches[pygame.K_a]: #SW
			N,S,E,W,NE,NW,SE,SW = False,False,False,False,False,False,False,True

		if touches[pygame.K_s] and touches[pygame.K_d]: #SE
			N,S,E,W,NE,NW,SE,SW = False,False,False,False,False,False,True,False

		return N,S,E,W,NE,NW,SE,SW

	def enVie(self):
		if self.vie <= 0:
			return False
		return True


class Enemys(ElementGraphique):
	def __init__(self, img, x, y, pouvoir, v, i, rebmax):
		super(Enemys, self).__init__(img, x, y)
		self.vx = v
		self.vy = v
		self.reb = 0
		self.pouvoir = pouvoir
		self.rebmax = rebmax
		self.apparition = i

	def Deplacer(self, hauteur, largeur, enemys, balle):
		rebond = False
		if self.rect.y + self.rect.h >= hauteur:
			self.vy = -abs(self.vy)
			rebond = True
		
		if self.rect.y < 0:
			self.vy = abs(self.vy)
			rebond = True

		if self.rect.x +self.rect.w >= largeur:
			self.vx = -abs(self.vx)
			rebond = True

		if self.rect.x <= 0:
			self.vx = abs(self.vx)
			rebond = True

		if rebond:
			self.reb += 1

		if self.reb == self.rebmax:
			enemys.remove(balle)

		self.rect.y += self.vy
		self.rect.x += self.vx
		
	def Deplacer2(self, perso):
		if self.rect.x > perso.rect.x and self.vx > -7:
			self.vx -= 1

		if self.rect.y > perso.rect.y and self.vy > -7:
			self.vy -= 1
		
		if self.rect.x < perso.rect.x and self.vx < 7:
			self.vx += 1

		if self.rect.y < perso.rect.y and self.vy < 7:
			self.vy += 1

		if self.rect.x == perso.rect.x:
			self.vx = 0

		if self.rect.y == perso.rect.y:
			self.vy = 0

		self.rect.x += self.vx
		self.rect.y += self.vy
	
			
	
	def Collisions(self, Perso, enemys, balle):
		if self.rect.colliderect(Perso.rect):
			if self.pouvoir == 0:
				enemys.remove(balle)
				Perso.vie -= 1
			
			if self.pouvoir == 1:
				enemys.clear()

			if self.pouvoir == 2:
				enemys.remove(balle)
				Perso.vie -= 2
			
			if self.pouvoir == 3:
				enemys.remove(balle)
				Perso.vie += 1


fondjeu = ElementGraphique(bank["background"], 0, 0)
perso = Perso(bank["tile000"], 960, 540)	

font = pygame.font.Font(None, 30)
font2 = pygame.font.Font("polices/airstrikeb3d.ttf", 100)
font3 = pygame.font.Font("polices/Ornamentmix.ttf", 100)

N,S,E,W,NE,NW,SE,SW = True,False,False,False,False,False,False,False

enemys = []

horloge = pygame.time.Clock()
i = 0
secondes = 0
state = 'Jeu'
continuer = True

while continuer:
	horloge.tick(144)
	i+=1

	touches = pygame.key.get_pressed()

	if touches[pygame.K_ESCAPE] :
		continuer=0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = 0

	if state == "Jeu":

		imagevie = font.render("Vies: "+str(perso.vie), 1, (255, 255, 255))		
		vie = ElementGraphique(imagevie, 0,5)

		imagetemps = font.render("Secondes: "+str(secondes), 1, (255, 255, 255))
		temps = ElementGraphique(imagetemps, 0,25)	

		if i %60 == 0:
			secondes += 1

		if i %90 == 0:
			nbr = random()
			if 0 <= nbr < 0.5:
				enemys.append(Enemys(bank["balle"] ,randint(0, largeur), randint(0, hauteur), 0, randint(5, 15), i, randint(2, 5)))

			if 0.5 <= nbr < 0.7:
				enemys.append(Enemys(bank["bonus"] ,randint(0, largeur), randint(0, hauteur), 1, randint(5, 15), i, randint(2, 5)))

			if 0.7 <= nbr < 0.85:
				enemys.append(Enemys(bank["mort"],randint(0, largeur), randint(0, hauteur), 2, randint(5, 15), i, randint(2, 5)))

			if 0.85 <= nbr <= 1:
				enemys.append(Enemys(bank["coeur"],randint(0, largeur), randint(0, hauteur), 3, randint(5, 15), i, randint(2, 5)))

		fondjeu.Afficher(fenetre)
		N,S,E,W,NE,NW,SE,SW = perso.Direction(touches, N,S,E,W,NE,NW,SE,SW)
		perso.Orientation(N,S,E,W,NE,NW,SE,SW)
		perso.Deplacer(touches, largeur, hauteur)
		vie.Afficher(fenetre)
		temps.Afficher(fenetre)
				
		for balle in enemys:
			balle.Afficher(fenetre)
			balle.Deplacer(hauteur, largeur, enemys, balle)

	pygame.display.update()

pygame.quit()