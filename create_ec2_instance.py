import boto3
import os

client=boto3.client('ec2')
	
# Create a new Ubuntu EC2 instance	
def ubuntu_instance():
	
	resp=client.run_instances(
		ImageId='ami-0998bf58313ab53da',
		MinCount=1,
		MaxCount=1,
		InstanceType='t2.micro',
		#KeyName='ec2-keypair'
	)

	for instance in resp['Instances']:
		print(instance['InstanceId'])

#Create a new Windows EC2 instance
def windows_instance():

	resp=client.run_instances(
		ImageId='ami-067317d2d40fd5919',
		MinCount=1,
		MaxCount=1,
		InstanceType='t2.micro',
		#KeyName='ec2-keypair'
	)

	for instance in resp['Instances']:
		print(instance['InstanceId'])

#Passing the choice of instance which you want to create(i.e. Linux or Windows)
def instance_type(ch):
    if ch==0:
    	ubuntu_instance()
    elif ch==1:
    	windows_instance()
    else:
    	return "Invalid choice of instance\n"

#Main function
def main():

	choice=int(input("""Enter the choice of instance you want to launch:
Press 0: For Ubuntu instance
Press 1: For Windows instance\n"""))
	if choice==0 or choice==1:
		instance_type(choice)
	else:
		print("Invalid choice! Please choose the correct choice")
		main()

