import cv2 as cv
from cvzone.HandTrackingModule import HandDetector as hdari
import pyaudio
import wave
from playsound import playsound
import pygame
import sys
import time

w,h = 1600,900
white = (255,255,255)

class TomCounts_ARI:
	def __init__(self):
		pygame.init()
		pygame.font.init()
		self.list = []
		self.font = pygame.font.Font("quake.ttf", 55)
		self.count = 0
		self.width = 1920
		self.height = 1080
		self.disp = pygame.display.set_mode((self.width,self.height),0,0)
		self.img = pygame.image.load("Speak/0001.jpg")
		self.img = pygame.transform.scale(self.img,(w-50,h-100))
		self.CAPTURE_ALL()

	def blitForever(self,val=None):
		if(val!=None):
			if(val not in self.list):
				self.list = []
				self.list.append(val)
				self.playAudioARI(val)
		else:
			self.disp.blit(self.img,(-0,150,0,0))
		pygame.display.update()

	def playAudioARI(self,op):
		i = 1
		playsound(op,False)
		while(True):
			text1 = self.font.render(op[9], True, white)
			text1Rect = text1.get_rect()
			text1Rect.center = (450, 880)
			img = pygame.image.load("Speak/0"+str(i).zfill(3)+".jpg")
			img = pygame.transform.scale(img,(w-50,h-100))
			self.disp.blit(img,(-0,150,0,0))
			self.disp.blit(text1,text1Rect)
			i+=1
			if(i==10):
				return
			pygame.display.update()

	def CAPTURE_ALL(self):
		CAM = cv.VideoCapture(0,cv.CAP_DSHOW)
		det = hdari(detectionCon=0.8,maxHands=1)
		while True:
			status,frame = CAM.read()
			frame = cv.flip(frame,1)
			hands,frame = det.findHands(frame,flipType=False)
			if hands:
				lmlist = hands[0]
				if lmlist:
					fingerup = det.fingersUp(lmlist)
					if fingerup == [0, 1, 0, 0, 0]:
						self.blitForever('SpeakAud/1.wav')
					if fingerup == [0, 1, 1, 0, 0]:
						self.blitForever('SpeakAud/2.wav')
					if fingerup == [0, 1, 1, 1, 0]:
						self.blitForever('SpeakAud/3.wav')
					if fingerup == [0, 1, 1, 1, 1]:
						self.blitForever('SpeakAud/4.wav')
					if fingerup == [1, 1, 1, 1, 1]:
						self.blitForever('SpeakAud/5.wav')
			self.blitForever()
			cv.imshow("Ari",frame)
			cv.waitKey(1)
			if cv.waitKey(1) & 0xFF == ord('q'):
				break
		cv.destroyAllWindows()

TomCounts_ARI()
