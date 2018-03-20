import pygame

import random

SCREEN_RECT = pygame.Rect(0,0,1200,622) 

ENEMY_EVENT = pygame.USEREVENT

HERO_BULLET_EVENT = pygame.USEREVENT + 1

class CuiShu_GameSprites(pygame.sprite.Sprite):

	#初始化精灵的 图片 位置 速度
	def __init__(self,new_image,speed=1):

		super().__init__()
		self.image = pygame.image.load(new_image)
		self.speed = speed

		self.rect = self.image.get_rect()
	def update(self):

		self.rect.x += self.speed

class CuiShu_BackGround(GameSprites):
	
	def __init__(self,is_alt=False):

		super().__init__("/home/share/air.jpg") 
		self.rect.left = 0
		
		if is_alt:
			self.rect.right = self.rect.left

	def update(self):

		super().update()

class CuiShu_Enemy(GameSprites):

	def __init__(self):
		super().__init__("./Runoob/images/enemy2.png")#---------------------------------------

		self.rect.right = SCREEN_RECT.left
		self.speed = random.randint(1,4)
		#设置范围
		max_y = SCREEN_RECT.height - self.rect.height
		self.rect.y = random.randint(0,max_y)

	def update(self):
		
		super().update()

		if self.rect.left == SCREEN_RECT.right:
			self.kill()

class CuiShu_Hero(GameSprites):

	def __init__(self):
		super().__init__("./Runoob/images/me1.png")
		self.rect.centery = SCREEN_RECT.centery
		self.rect.right = SCREEN_RECT.right
		#创建主机子弹精灵组
		self.bullets = pygame.sprite.Group()
		#僚机位置
		self.wingman1 = WingMan()
		self.wingman2 = WingMan()
		self.wingman1.rect.right = SCREEN_RECT.right
		self.wingman2.rect.right = SCREEN_RECT.right
		self.wingman1.rect.top = self.rect.bottom
		self.wingman2.rect.bottom = self.rect.top
		#创建僚机子弹精灵组
		self.bullet1_group = pygame.sprite.Group()
		self.bullet2_group = pygame.sprite.Group()

		#创建僚机精灵组
		
		self.wingman1_group = pygame.sprite.Group(self.wingman1)
		
		self.wingman2_group = pygame.sprite.Group(self.wingman2)
	def update(self):
		#主机	
		self.rect.y += self.speed
		if self.rect.top < SCREEN_RECT.top + self.wingman2.rect.height:
			self.rect.top = SCREEN_RECT.top + self.wingman2.rect.height
		elif self.rect.bottom > SCREEN_RECT.bottom - self.wingman1.rect.height:
			self.rect.bottom = SCREEN_RECT.bottom - self.wingman1.rect.height
		#僚机
		if self.wingman2.rect.top <= SCREEN_RECT.top:
			self.wingman2.rect.top = SCREEN_RECT.top
		elif self.wingman2.rect.bottom >= self.rect.top:
			self.wingman2.rect.bottom = self.rect.top
		if self.wingman1.rect.bottom >= SCREEN_RECT.bottom:
			self.wingman1.rect.bottom = SCREEN_RECT.bottom
		elif self.wingman1.rect.top <= self.rect.bottom:
			self.wingman1.rect.top = self.rect.bottom 	
	def fire(self):
		for num in range(1,4):
			bullet = Bullet()
			self.bullet1 = Bullet()
			self.bullet2 = Bullet()

			bullet.rect.centery = self.rect.centery
			bullet.rect.right = self.rect.left - 20 * num
			self.bullet1.rect.centery = self.wingman1.rect.centery
			self.bullet1.rect.right = self.wingman1.rect.left - 10 * num
			self.bullet2.rect.centery = self.wingman2.rect.centery 
			self.bullet2.rect.right =  self.wingman2.rect.left - 10 * num
			self.bullets.add(bullet)
			self.bullet1_group.add(self.bullet1)
			self.bullet2_group.add(self.bullet2)
	
class CuiShu_Bullet(GameSprites):

	def __init__(self):
		super().__init__("./Runoob/images/bullet2.png",-2)

	def update(self):
		super().update()
		if self.rect.right <= SCREEN_RECT.left:
			self.kill()

"""僚机"""
class CuiShu_WingMan(GameSprites):

	def __init__(self):
		super().__init__("./Runoob/images/life.png",-1)

	def update(self):
		self.rect.y += self.speed
