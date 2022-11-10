import boto3

ec2_client=boto3.client("ec2")

x=ec2_client.describe_