import pygame, os
from math import atan2, pi
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

	def Afficher(self, window, image, rect) :
		window.blit(image, rect)



class Perso(ElementGraphique):
	def __init__(self, img, x, y):
		super(Perso, self).__init__(img, x, y)
		self.rot_image = img
		self.rect2 = self.image.get_rect()
		self.angle = 0
		self.vitesse = 10


	def Orientation(self, mx, my):
		self.angle = atan2(my - 540, mx - 960)
		self.rot_image = pygame.transform.rotate(self.image, -self.angle/pi*180)
		self.rect2 = self.rot_image.get_rect(center = self.rect.center)

	def Deplacer(self, touches, largeur, hauteur):
		if touches[pygame.K_d] and self.rect.x <= largeur-self.rect.w:
			self.rect.x += self.vitesse
		if touches[pygame.K_a] and self.rect.x >= 0:
			self.rect.x -= self.vitesse
		if touches[pygame.K_w] and self.rect.y >= 0:
			self.rect.y -= self.vitesse
		if touches[pygame.K_s] and self.rect.y <= hauteur-self.rect.h:
			self.rect.y += self.vitesse


horloge = pygame.time.Clock()

fondjeu = ElementGraphique(bank["background"], 0, 0)
perso = Perso(bank["tile000"], 960, 540)

continuer = True
state = 'Jeu'

while continuer:
	horloge.tick(30)
	touches = pygame.key.get_pressed()

	if touches[pygame.K_ESCAPE] :
		continuer=0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = 0
	
	if state == "Jeu":
		mx, my = pygame.mouse.get_pos()

		fondjeu.Afficher(fenetre, fondjeu.image, fondjeu.rect)
		perso.Afficher(fenetre, perso.rot_image, perso.rect2)
		perso.Orientation(mx, my)
		perso.Deplacer(touches, largeur, hauteur)


	pygame.display.update()