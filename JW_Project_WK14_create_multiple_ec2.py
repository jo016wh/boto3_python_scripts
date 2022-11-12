import boto3
client = boto3.client('ec2')
resp=client.run_instances(ImageId='ami-09d3b3274b6c5d4aa',
        InstanceType='t2.micro',
        MinCount=3,
        MaxCount=3,
        SubnetId='subnet-0a2113bd7f264a574',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name','Value': 'JW Week 14 Project'},
                {'Key': 'Env','Value': 'Dev'}]
                          },
                      ],
                      )
for i in resp['Instances']:
    print("Instance ID Created is :{} Instance Type Created is : {}" .format(i['InstanceId'],i['InstanceType']))
    