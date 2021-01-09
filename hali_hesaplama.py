import math


def hali_hesaplama():
	oda = input()
	try: 
		int(oda)
	except ValueError:
		print("Lutfen tam sayi ve pozitif bir deger giriniz.")
		return
	else:
		if oda.find(".") != -1 or oda.find(",") != -1 or int(oda)<=0:
			print("Lutfen tam sayi ve pozitif bir deger giriniz.")
			return 

		oda = int(oda)
		output = []

		while oda:
			kare = math.sqrt(oda)
			kare = int(kare)
			output.append(kare)
			oda = oda -(kare*kare)
			
		s = ""	 
		for i in range(0,len(output)):
			if i != len(output)-1:
				s = s + str(output[i]*output[i]) + ", "
			else:
				s = s +str(output[i]*output[i])
		print(s)

hali_hesaplama()
