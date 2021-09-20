'''ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการใช้ Class สำหรับ “เกมต่อคำ” โดยจะมีกติกาดังต่อไปนี้

 
1. คำล่าสุดจะต้องไม่ซ้ำกับคำที่เคยพูดไปแล้ว เช่นถ้าหากมีคนพูดว่า “Apple” ไปก่อนหน้านั้นแล้ว
จะไม่สามารถพูดว่า “Apple” ได้อีก


2. โดยการดูว่า 2 คำนั้นจะ Match กันหรือไม่ ให้ดู 2 ตัวอักษรสุดท้ายของข้อความสุดท้ายใน List กับ 2
ตัวอักษรแรก ของคำล่าสุด เช่น [“Apple”, “lemon”] ถ้าหากคำที่จะเข้ามาเป็น “Onion” จะถือว่า Match
แต่ถ้าหากคำที่เข้ามาเป็น “nectarine” จะถือว่าไม่ Match และเกมจะจบลงทันที


3. Ignore Case Sensitive


โดยจะมีรูปแบบคำสั่งดังต่อไปนี้
- P < word > จะเป็นการต่อคำ
- R จะเป็นการเริ่มคำใหม่ทั้งหมด
- X เป็นการระบุว่าจบการทำงาน

โดยใช้ class รูปแบบดังนี้

class TorKham:

	def __init__(self):

		self.words = []

	def restart(self):

		 ### Enter Your Code Here ###

		return "game restarted"

	def play(self, word):

		 ### Enter Your Code Here ###

		return "game over"



torkham = TorKham()

print("*** TorKham HanSaa ***")


S = input("Enter Input : ").split(',')

 ### Enter Your Code Here ###'''
 
class TorKham:

	def __init__(self):
		self.words = []

	def restart(self):
		self.words = []
		return "game restarted"

	def play(self, word):
		for self.i in self.words:
			if self.i == word:
				return "a game over"
		self.words.append(word)
		self.temp = self.words[len(self.words)-2]
		if len(self.words) == 1:
			return str(self.words)
		elif self.temp[len(self.temp)-2].lower()==word[0].lower() and self.temp[len(self.temp)-1].lower()==word[1].lower():
			return str(self.words)
		else:
			return "game over"



torkham = TorKham()

print("*** TorKham HanSaa ***")

S = input("Enter Input : ").split(',')
for i in S:
	if i[0] == 'R':
		print(torkham.restart())
	elif i[0] == 'P':
		char,temp = i.split()
		print("\'"+temp+"\'"+" -> "+torkham.play(temp))
	elif i[0] == 'X':
		break
	else:
		print("\'"+i+"\'"+" is Invalid Input !!!")
		break
