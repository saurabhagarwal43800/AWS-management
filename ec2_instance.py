import boto3
import os
import time
import sys

def get_ec2_con_for_give_region(my_region):
	ec2_con_re=boto3.resource('ec2',region_name=my_region)
	return ec2_con_re

def list_instances_on_my_region(ec2_con_re):
	for each in ec2_con_re.instances.all():
		print(each.id)

def get_instant_state(ec2_con_re,in_id):
	for each in ec2_con_re.instances.filter(Filters=[{'Name':'instance-id','Values':[in_id]}]):
		pr_st=each.state['Name']
	return pr_st

def start_instance(ec2_con_re,in_id):
	pr_st=get_instant_state(ec2_con_re,in_id)
	if pr_st=="running":
		print("instance is already runing")
	else:
		for each in ec2_con_re.instances.filter(Filters=[{'Name':'instance-id','Values':[in_id]}]):
			each.start()
			print("Please wait it is going to start, once if it is started then we will let you know")
			each.wait_until_running()
			print("now it is running")
	return

def Thank_You():
	print("\n\n*********Thank You for using this Script*********")
	return None

def stop_instance(ec2_con_re,in_id):
	pr_st=get_instant_state(ec2_con_re,in_id)
	if pr_st=="stopped":
		print("instance is already stopped")
	else:
		for each in ec2_con_re.instances.filter(Filters=[{'Name':'instance-id','Values':[in_id]}]):
			each.stop()
			print("Please wait it is going to stop, once if it is stopped then we will let you know")
			each.wait_until_stopped()
			print("now it is stopped")

def welcome():
	print("This script will help you to start or stop ec2 instance based on your required region and instance id")
	print("Enjoy by using this script\n\n")
	time.sleep(3)

def main():
	welcome()
	my_region=input("Enter your region name")
	print("please wait.....connecting to your aws ec2 console.....")
	ec2_con_re=get_ec2_con_for_give_region(my_region)
	print("please wait listing all instances ids in your region {}".format(my_region))
	list_instances_on_my_region(ec2_con_re)
	in_id=input("Now choose your instance id to start or stop:")
	start_stop=input("Enter either stop or start command for your ec2 instance:")
	while True:
		if start_stop not in ["start","stop"]:
			start_stop=input("Enter only start or stop commands:")
			continue
		else:
			break
	if start_stop=="start":
		start_instance(ec2_con_re,in_id)
	else:
		stop_instance(ec2_con_re,in_id)
	Thank_You()


if __name__ == '__main__':
	os.system('cls')
	main() 
