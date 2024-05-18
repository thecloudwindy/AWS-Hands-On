import boto3
from pprint import *

def iam_client():
    iam = boto3.client('iam')
    return iam

def create_group(group_name):
    response = iam_client().create_group(
        GroupName = group_name
    )
    return response

if __name__ == "__main__":
    group_name = input("Enter the name of group: ")
    result = create_group(group_name)
    pprint(result)

