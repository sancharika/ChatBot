import pyttsx3
import os
import smtplib

pyttsx3.speak("Welcome to my assistant ")


while True:
	print("Enter your choice : " , end=" ")
	pyttsx3.speak("Enter your choice")
	p=input()
	#Alexa-Holes
	
	if   (("notepad" in p)or ("editor" in p)):
		pyttsx3.speak("Opening Notepad")
		os.system("notepad")
	elif  (("chorme" in p)or ("google" in p)):
		pyttsx3.speak("Opening google chrome")
		os.system("start chrome ")
		pyttsx3.speak("Done")
	elif  (("cal" in p)or ("calculator" in p)):
		pyttsx3.speak("Opening calculator")
		os.system("start calculator ")
		pyttsx3.speak("Done")
	elif  (("cmd" in p)or ("command" in p)):
		pyttsx3.speak("Opening command prompt")
		os.system("start cmd prompt ")
		pyttsx3.speak("Done")	
	elif (("exit" in p) or ("quit" in p)):
		pyttsx3.speak("good bye, have a nice day")
		break
	else : 
		print("Not support")
		pyttsx3.speak("sorry ! I can't understand you ")




















