import random

class CuiShu_cai(object):

	def __init__(self):

		self.computer = random.randint(0,99)
		self.again = 1
		self.count = 0
		self.count_list = []
	def CuiShu_panduan(self):

		while True:
			self.count += 1
			self.person = int(input("请输入一个整数: "))

			if self.person == self.computer:
				print("恭喜猜中了,还要继续吗?")
				choice = int(input("1:继续 2:结束"))
				if choice == 1:
					self.again += 1
					self.count_list.append(self.count)
					self.count = 0
				if choice == 2:
					self.count_list.append(self.count)
					break
					self.Cuishu_jisuan()
			elif self.person > self.computer:
				print("你猜的数字有点大")

			else:
				print("你猜的数字有点小")

	def Cuishu_print(self):

		#共玩了多少次
		print("一共玩了" + str(self.again) + "次.")
		#每次各猜了几次猜中
		for num in self.count_list:
			
			print("每次各猜了" + str(num) + "次.")
			num += num
		#平均猜中的次数
		if self.again == 1:
			sum_number = (num / 2) / self.again
			print("平均每次猜了" + str(sum_number) + "次才猜中.")
		elif self.again > 1:
			sum_number = num / self.again
			print("平均每次猜了" + str(sum_number) + "次才猜中.")

CuiShu = CuiShu_cai()
CuiShu.CuiShu_panduan()
CuiShu.Cuishu_print()