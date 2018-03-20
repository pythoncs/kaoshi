import pygame

from kao2 import *

class CuiShu_PlaneGame(object):

	def __init__(self):
		#创建游戏窗口
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		#设置时钟
		self.clock = pygame.time.Clock()
		#创建精灵 精灵组
		self.__creat_sprite()

		pygame.time.set_timer(ENEMY_EVENT,1000)
		pygame.time.set_timer(HERO_BULLET_EVENT,500)

		self.count = 0
	
	def start_game(self):
		
		while True:
			#设置帧率
			self.clock.tick(60)
			#事件监听
			self.__event_handler()
			#碰撞检测
			self.__check_collide()
			#更新精灵组
			self.__sprites_update()
			#更新屏幕
			pygame.display.update()

	def game_over(self):
		pygame.quit()
		exit()

	def __creat_sprite(self):
		#创建精灵 精灵组
		png1 = BackGround()
		png2 = BackGround(True)
		self.back_group = pygame.sprite.Group(png1,png2)

		self.enemy = Enemy()
		self.enemy_group = pygame.sprite.Group(self.enemy)

		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)

		
	def __event_handler(self):
		for event in pygame.event.get():
			my_pressed = pygame.key.get_pressed()
			if my_pressed[pygame.K_UP]:
				self.hero.speed = -5
				self.hero.wingman1.speed = -5
				self.hero.wingman2.speed = -5
			elif my_pressed[pygame.K_DOWN]:
				self.hero.speed = 5
				self.hero.wingman1.speed = 5
				self.hero.wingman2.speed = 5
			else:
				self.hero.speed = 0
				self.hero.wingman1.speed = 0
				self.hero.wingman2.speed = 0
			if event.type == pygame.QUIT:
				self.game_over()
			elif event.type == ENEMY_EVENT:
				self.enemy_group.add(Enemy())
				print(self.enemy_group)
			elif event.type == HERO_BULLET_EVENT:
				self.hero.fire()

	def __check_collide(self):
		#碰撞检测
		a = pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
		hero_collide = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		wingman11 = pygame.sprite.groupcollide(self.hero.wingman1_group,self.enemy_group,True,True)
		wingman22 = pygame.sprite.groupcollide(self.hero.wingman2_group,self.enemy_group,True,True)
		bullet11 = pygame.sprite.groupcollide(self.hero.bullet1_group,self.enemy_group,True,True)
		bullet22 = pygame.sprite.groupcollide(self.hero.bullet2_group,self.enemy_group,True,True)
		
		if len(hero_collide) > 0:
			self.hero.kill()
			pygame.quit()
			exit()
		if len(wingman11) > 0:
			self.hero.wingman1.rect.y = 10000
			self.hero.wingman1.kill()

		if len(wingman22) > 0:
			self.hero.wingman2.rect.y = -10000
			self.hero.wingman2.kill()

		if len(bullet11) > 0 or len(bullet22) > 0 or len(a) > 0:
			self.count += 1
			print("击毁" + str(self.count) + "架敌机")
	def __sprites_update(self):
		#更新精灵 精灵组
		self.back_group.update()
		self.back_group.draw(self.screen)

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.hero_group.update()
		self.hero_group.draw(self.screen)

		self.hero.wingman1_group.update()
		self.hero.wingman1_group.draw(self.screen)
		
		self.hero.wingman2_group.update()
		self.hero.wingman2_group.draw(self.screen)

		self.hero.bullets.update()
		self.hero.bullets.draw(self.screen)

		self.hero.bullet1_group.update()
		self.hero.bullet1_group.draw(self.screen)
		
		self.hero.bullet2_group.update()
		self.hero.bullet2_group.draw(self.screen)
		

if __name__ == "__main__":

	game = CuiShu_PlaneGame()

	game.start_game()