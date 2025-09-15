import boto3
from botocore.exceptions import NoCredentialsError, NoRegionError

try:
	ec2 = boto3.resource('ec2')
	for instance in ec2.instances.all():
		print(f'Instance ID: {instance.id}, State: {instance.state["Name"]}')
except NoCredentialsError:
	print("AWS credentials not found. Please configure your credentials.")
except NoRegionError:
	print("AWS region not specified. Please configure your region.")
except Exception as e:
	print(f"An error occurred: {e}")
	
	# Filter to get only running instances; adjust 'Values' as needed for other states
	instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
	for instance in instances:
		print(f'Instance ID: {instance.id}, State: {instance.state["Name"]}')
from botocore.exceptions import NoCredentialsError, ClientError

try:
	ec2 = boto3.resource('ec2')

	for instance in ec2.instances.all():
		print(f'Instance ID: {instance.id}, State: {instance.state["Name"]}')
except NoCredentialsError:
	print("AWS credentials not found. Please configure your credentials.")
except ClientError as e:
	print(f"AWS ClientError: {e}")
except Exception as e:
	print(f"An unexpected error occurred: {e}")
