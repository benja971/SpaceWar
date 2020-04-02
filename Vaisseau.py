import pygame, json, os
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

bank = getImgBank("images")

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
		self.vitesse = 10
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




fondjeu = ElementGraphique(bank["background"], 0, 0)
perso = Perso(bank["tile000"], 960, 540)	

N,S,E,W,NE,NW,SE,SW = True,False,False,False,False,False,False,False

horloge = pygame.time.Clock()
i = 0

state = 'Jeu'
continuer = True

while continuer:
	horloge.tick(30)
	i+=1

	touches = pygame.key.get_pressed()

	if touches[pygame.K_ESCAPE] :
		continuer=0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = 0

	if state == "Jeu":

		fondjeu.Afficher(fenetre)
		N,S,E,W,NE,NW,SE,SW = perso.Direction(touches, N,S,E,W,NE,NW,SE,SW)
		perso.Orientation(N,S,E,W,NE,NW,SE,SW)
		perso.Deplacer(touches, largeur, hauteur)

	pygame.display.update()

pygame.quit()