import boto3 
from pprint import * 

def iam_client():
    iam = boto3.client('iam')
    return iam 

def create_access_key(username):
    response = iam_client().create_access_key(
        UserName= username
    )
    return response

if __name__ == "__main__":
    username = "dev-user"
    result = create_access_key(username)
    pprint(result) 

