import pyttsx3
import os
import numpy

pyttsx3.speak("Welcome To Mini Application to know the information of Mobile Devices")
print("\t\t\t`````````````````````````````````````````````````````````````````````")
print("\t\t\t  Welcome To Mini Application to know the information of Mobile Device  ")
print("\n\t\t\t`````````````````````````````````````````````````````````````````````")

while True:
	print("\t\t\t\t   ||==========================================||")
	print("\t\t\t\t   ||\t\tSelect Your Choice             ||")
	print("\t\t\t\t   ||==========================================||")
	print("\t\t\t\t   || 1. List of mobile brand.                 ||")
	print("\t\t\t\t   || 2. List of mobile brand with price range.||")
	print("\t\t\t\t   || 3. Information of the mobile.            ||")
	print("\t\t\t\t   || 4. Exit.                                 ||")
	print("\t\t\t\t   ||==========================================||")

	pyttsx3.speak("Select Your choice")
	print("==>>Select Your choice:",end='')
	c=input()
#c is for the choice
	if("1" in c):	
		pyttsx3.speak("Currently we only have the following mobile brand.")
		print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
		print("|Currently we only have the following mobile brand.|")
		print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
		print("|\t\t 1.Samsung                         |")
		print("|\t\t 2.Nokia                           |")
		print("|\t\t 3.Oneplus                         |")
		print("|\t\t 4.Huawei                          |")
		print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
	elif("2" in c):
		print("\n=>Here is the list of mobile devices with price range.")
		pyttsx3.speak("Here is the list of mobile devices with price range.")
		print("\n************************************************************************")
		print(" Sr.No","\t\t Name","\t\tPrice Range(In Rs.)")
		print("************************************************************************")
		print(" 1.", "\t\t Samsung", "\t 10,000/- to 70,000/-")
		print(" 2.", "\t\t Nokia", "\t\t 1000/- to 10,000/-")
		print(" 3.", "\t\t OnePlus", "\t 10,000/- to 60,000/-")
		print(" 4.", "\t\t Huawei", "\t 30,000/- to 1,00,000/-")
		print("************************************************************************")
	elif("3" in c):	
		pyttsx3.speak("Currently we only have the following mobile brand.")
		print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
		print("|Currently we only have the following mobile brand.|")
		print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
		print("|\t\t 1.Samsung                         |")
		print("|\t\t 2.Nokia                           |")
		print("|\t\t 3.Oneplus                         |")
		print("|\t\t 4.Huawei                          |")
		print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
		print("==>>Select from the above to know the information of the mobile :",end='')

		pyttsx3.speak("Select from the above to know the information of the mobile")
		s=input()
#s is for the selection	

		if("1" or "Samsung" in s):
			print("\n=>Here is the list of AVAILABLE SAMSUNG mobile.")
			pyttsx3.speak("Here is the list of AVAILABLE SAMSUNG mobile")
			print("\n..........................................................................")
			print(" SR.No","\t  NAME","\t\t RAM,GB,COLOR","\t\t PRICE(IN Rs.)")
			print("..........................................................................")
			print(" 1.", "\t Samsung s8","\t 4GB RAM,64GB,Black", "\t 25,999/-")
			print(" 2.", "\t Samsung s9","\t 4GB RAM,64GB,Purple", "\t 65,000/-")
			print(" 3.", "\t Samsung s10","\t 4GB RAM,64GB,White", "\t 47,999/-")
			print(" 4.", "\t Samsung s20","\t 4GB RAM,64GB,Blue","\t 70,000/-")
			print("..........................................................................")

		elif("2" or "Nokia" in s):
			print("\n=>Here is the list of AVAILABLE NOKIA mobile.")
			pyttsx3.speak("Here is the list of AVAILABLE NOKIA mobile")
			print("\n..........................................................................")
			print(" SR.No","\t  NAME","\t\t RAM,GB,COLOR","\t\t PRICE(IN Rs.)")
			print("..........................................................................")
			print(" 1.", "\t Nokia 5310","\t 4GB RAM,64GB,Blue", "\t 3,399/-")
			print(" 2.", "\t Nokia 2.3","\t 4GB RAM,64GB,Red", "\t 8,790/-")
			print(" 3.", "\t Nokia 110","\t 4GB RAM,64GB,Grey", "\t 1,599/-")
			print(" 4.", "\t Nokia 6.2","\t 4GB RAM,64GB,Black","\t 12,849/-")
			print("..........................................................................")

		elif("3" or "Oneplus" in s):
			print("\n=>Here is the list of AVAILABLE ONEPLUS mobile.")
			pyttsx3.speak("Here is the list of AVAILABLE ONEPLUS mobile")
			print("\n..........................................................................")
			print(" SR.No","\t  NAME","\t\t RAM,GB,COLOR","\t\t PRICE(IN Rs.)")
			print("..........................................................................")
			print(" 1.", "\t Oneplus 7T","\t 4GB RAM,64GB,White", "\t 47,999/-")
			print(" 2.", "\t Oneplus 7T Pro","\t 4GB RAM,64GB,Violet", "\t 54,999/-")
			print(" 3.", "\t Oneplus 8","\t 4GB RAM,64GB,Red", "\t 41,999/-")
			print(" 4.", "\t Oneplus 8 Pro","\t 4GB RAM,64GB,Black","\t 58,999/-")
			print("..........................................................................")
	
		elif("4" or "Huawei" in s):
			print("=>\nHere is the list of AVAILABLE HUAWEI mobile.")
			pyttsx3.speak("Here is the list of AVAILABLE HUAWEI mobile")
			print("\n..........................................................................")
			print(" SR.No","\t  NAME","\t\t RAM,GB,COLOR","\t\t PRICE(IN Rs.)")
			print("..........................................................................")
			print(" 1.", "\t Huawei 7","\t 4GB RAM,64GB,Black", "\t 25,999/-")
			print(" 2.", "\t Huawei 8","\t 4GB RAM,64GB,Purple", "\t 65,000/-")
			print(" 3.", "\t Huawei X","\t 4GB RAM,64GB,White", "\t 47,999/-")
			print(" 4.", "\t Huawei 11","\t 4GB RAM,64GB,Black","\t 70,000/-")
			print("..........................................................................")

		elif("5" or "6" or "7" or "8" or "iphone" or "Iphone" or "apple" or "Apple" or "oppo" or "Oppo" or "Redmi" or "redmi" or "Realme" or "realme" or "Asus" or "asus"):
			print("\n Sorry for the inconvenience , we do not have the requested device")
			pyttsx3.speak("Sorry for the inconvenience , we do not have the requested device")
		else:
			print("###############")
			print("Your Choice is invalid.")
			print("###############")
			pyttsx3.speak("Your Choice is invalid.")
	elif("4" in c):
		print("Thank you for using the application.")
		pyttsx3.speak("Thank you for using the application.")
		break
	else:
		print("###############")
		print("Your Choice is invalid.")
		print("###############")
		pyttsx3.speak("Your Choice is invalid.")
	
		


