'''
โจทย์: จงเขียนโปรแกรมรับความเร็วลมเฉลี่ยใน 10 นาที และแสดงผลระดับพายุที่เกิดขึ้น จากการจัดแบ่งความเร็วลมดังนี้

		Speed (km/h)		ระดับพายุ
			0-51.99			Breeze
			52.00-55.99		Depression
			56.00-101.99	Tropical Storm
			102.00-208.99   Typhoon
			>= 209			Super Typhoon

โดยแสดงผลตามตัวอย่างการแสดงผล
'''
print(" *** Wind classification ***")
x = float(input("Enter wind speed (km/h) : "))
print("Wind classification is ",end="")
if x>=0 and x<52:
    print("Breeze.")
elif x<56:
    print("Depression.")
elif x<102:
    print("Tropical Storm.")
elif x<209:
    print("Typhoon.")
else:
    print("Super Typhoon.")