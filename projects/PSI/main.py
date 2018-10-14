#python 3.6
#
#Projet de Sciences de l'ingenieur DURAND Ulysse TS1 : Scanner 3d
#
#Programme qui vient afficher le rendu de l'acquisition du scanner 3d


import os, sys, pygame
from classes import *
from pygame.locals import *
from math import *

size = width, height = 600,600
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Projet SI scanner3d")


lss = 0
theta = 0
focal = 200
keypressed = {}
camera = [0,0,-200,2*3.14,0]
vecteurdroite = Vector([])
vecteurdevant = Vector([])
speed = 1
plane = []



class Line:
	def __init__(self,a,b,c,sw):
		self.a = a
		self.b = b
		self.c = c
		self.sw = sw

	def display(self):
		Drawing.line(self.a,self.b,self.c,self.sw)

class Point:
	def __init__(self,vec,c,sw):
		self.c = c
		self.sw = sw
		self.vec = vec

	def display(self):
		Drawing.ellipse(self.vec,self.c,self.sw)

class Drawing:
	def applyperspective(vec,w):
		a = Transform.perspective(w,vec.z)
		b = vec.tomatrix()
		res = a.multiply(b)
		res = res.tovector()
		return res

	def getinorigine(vec):
		return vec.add(Vector([width/2,height/2,0]))

	def apply3dstuff(vec):
		vec = Drawing.applyperspective(vec,focal)
		vec = Drawing.getinorigine(vec)
		return vec


	def ellipse(pos,color,radius):
		if (pos.z>=0):
			pos = Drawing.apply3dstuff(pos)
			pygame.draw.circle(screen,color,(int(pos.x),int(pos.y)),radius,0)

	def line(posa, posb, color, strokeweight):
		if (posa.z>=0 and posb.z >=0):
			posa = Drawing.apply3dstuff(posa)
			posb = Drawing.apply3dstuff(posb)
			pygame.draw.line(screen, color, [int(posa.x),int(posa.y)], [int(posb.x),int(posb.y)],strokeweight)


def main():
	setup()
	while True:
		loop()

def setup():
	lss = width
	if height<width:
		lss = height



def loop():
	events()
	draw()
	pygame.display.update()

def draw():
	global theta
	theta+=0.01
	screen.fill([255,255,255])
	vecteurdroite.x = cos(camera[4])
	vecteurdroite.z = sin(camera[4])
	points = []
	lines = []

	color = [0,0,0]

	origin = Vector([0,0,0])

	for i in range(2):
		for j in range(2):
			for k in range(2):
				points.append(Point(Vector([i*100-50,j*100-50,k*100-50]),color,2))

	for point in points:
		# point.vec = point.vec.rotate(theta,theta,theta)
		point.vec = point.vec.translate(Vector([-camera[0],camera[1],-camera[2]]))
		point.vec = point.vec.rotate(-camera[3],camera[4],0)


	lines.append(Line(points[0].vec,points[1].vec,color,2))
	lines.append(Line(points[2].vec,points[3].vec,color,2))
	lines.append(Line(points[1].vec,points[3].vec,color,2))
	lines.append(Line(points[0].vec,points[2].vec,color,2))
	lines.append(Line(points[4].vec,points[5].vec,color,2))
	lines.append(Line(points[6].vec,points[7].vec,color,2))
	lines.append(Line(points[5].vec,points[7].vec,color,2))
	lines.append(Line(points[4].vec,points[6].vec,color,2))
	lines.append(Line(points[0].vec,points[4].vec,color,2))
	lines.append(Line(points[1].vec,points[5].vec,color,2))
	lines.append(Line(points[2].vec,points[6].vec,color,2))
	lines.append(Line(points[3].vec,points[7].vec,color,2))


	for point in points:
		point.display()

	for line in lines:
		line.display()


def events():
	pygame.time.Clock().tick(60)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.display.quit()
			sys.exit(0)
		if event.type == KEYDOWN:
			keypressed[event.key] = True
		if event.type == KEYUP:
			keypressed[event.key] = False
		if event.type==MOUSEBUTTONDOWN:
			keypressed["mouse"+str(event.button)] = True
		if event.type==MOUSEBUTTONUP:
			keypressed["mouse"+str(event.button)] = False



		if event.type == MOUSEMOTION and "mouse3" in keypressed and keypressed["mouse3"]:
			camera[3] = -(event.pos[1]-height/2)/100
			camera[4] = -(event.pos[0]-width/2)/100

	if K_a in keypressed and keypressed[K_a]:
		camera[0]-=vecteurdroite.x
		camera[2]-=vecteurdroite.z

	if K_d in keypressed and keypressed[K_d]:
		camera[0]+=vecteurdroite.x
		camera[2]+=vecteurdroite.z

	if K_w in keypressed and keypressed[K_w]:
		camera[2]+=speed

	if K_s in keypressed and keypressed[K_s]:
		camera[2]-=speed

	if K_SPACE in keypressed and keypressed[K_SPACE]:
		camera[1]+=speed

	if K_LSHIFT in keypressed and keypressed[K_LSHIFT]:
		camera[1]-=speed



if __name__=="__main__":
	main()