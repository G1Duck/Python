#  Project Infinity
import time
Number = 0
print("Welcome to the Infinity project!")
time.sleep(1.5)
print("How high do you want to go today?")
Max = int(input())
while(Number <= Max):
	print(Number)
	Number = Number + 1
	time.sleep(0.2)

