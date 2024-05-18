import boto3
from pprint import *

def iam_client():
    iam = boto3.client('iam')
    return iam

def add_user_to_group(username, groupname):
    response = iam_client().add_user_to_group(
        GroupName= groupname,
        UserName= username
    )
    return response

if __name__ == "__main__":
    username = "dev-user"
    groupname = "dev-group"
    result = add_user_to_group(username, groupname)
    pprint(result)
