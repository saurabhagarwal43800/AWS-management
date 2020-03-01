import create_ec2_instance
import ec2_instance
import os
import sys
import time

'''To provide choice to the user whether he wants to create the instance or 
change the state to stop or start of the existing instance'''
def state_choice(st_ch):
        if st_ch==0:
        	create_ec2_instance.main()
        elif st_ch==1:
        	ec2_instance.main()

#Defining main function where he enters the choice to perform the state_choice function
def main():
	print("Welcome to the portal where you can work on AWS EC2 instance")
	print("************************************************************\n")

	state_ch=int(input("""Enter the choice that you want to create instance or change the state of instance,
Press 0: For creating instance
Press 1: For changing the state of existing instance\n"""))
	if state_ch==0 or state_ch==1:
		state_choice(state_ch)
	else:
		print("Invalid Choice! Please select the correct choice")
		main()

#Provide choice to again run the program or exit the program
def status():
		l1=int(input("""Press 0, If you want to run the program: \nPress 1, If you want to exit the program\n"""))
		if l1==0:
			loop()
		elif l1==1:
			print("*********Thanks for using this Script*********\n")
			time.sleep(1)
			exit()
		else:
			print("Invalid Choice\n")
			status()

#Starting point of the program
def loop():
	if __name__ == '__main__':
			os.system('cls')
			main()
			status()

loop()
