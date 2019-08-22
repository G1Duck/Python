from os import system
import sys

# Age Calculator
MH = 13
MC = 5
P = 5
D = 28
T = 36

Total = MH + MC + P + D +T
print("Total age of house is ", Total, " years old")


# Poo Calculator
system("clear")
print("Who are you calculating for?")

Pooper = input()
if Pooper =="Michael" or Pooper =="michael":
	print("Oh frick off you dingus!")
	sys.exit()
elif Pooper =="Dad":
	while(1):
		print("9999999999999999999999999999999999999999999999999999999999999")
	end

	sys.exit()

print("So you are calculating for ", Pooper)
print("How long is each poo? (Only put the number please)")

Length = int(input())
Year = 365
Mins = Length * Year

print(Pooper, " spends ", Mins,  " Minutes poopin")

Hour_In_Day = 24
Min_In_Hour = 60
Months = 12
Extra = 3
Indian_Time = Months * Extra * Length
print(Pooper, " spends ", Indian_Time, " Extra curry minutes")

print(Pooper, " spends ", Indian_Time + Mins, " Grand minutes of poopin")

Total_Poop_Minutes = Indian_Time + Mins
Total_Poop_Hours = Total_Poop_Minutes / Min_In_Hour
print(Pooper, " spends ", Total_Poop_Hours, " Grand amount of hours poopin")

Total_Days_Poopin = Total_Poop_Hours / Hour_In_Day
print(Pooper, " spends ",  Total_Days_Poopin, " Days pooped")
