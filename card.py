import random
card_turple = ('武则天','嬴政','诸葛亮','宫本武藏','李白','庄周','妲己')
package=[]

while True:
	choose=int(input('''
	氪金能让你变得更强!
	请输入指令:
	1. 抽卡
	2. 检查背包
	3. 整理背包
	4. 离开
	'''))
	if choose == 1:
		num=int(input('请输入抽卡次数:'))
		for i in range(0,num):
			n=random.randint(0,6)
			print('你抽到了:{}'.format(card_turple[n]))
			package.append(card_turple[n])
	if choose == 2:
		if len(package)==0:
			print('背包暂无英雄,请先去抽卡吧!')
		else:
			print(package)
	if choose == 3:
		if len(package)==0:
			print('背包暂无英雄,请先去抽卡吧!')
		else:
			package.sort()
			for i in package:
				print(i)
			print('__________________')		
	if choose == 4:
		break

