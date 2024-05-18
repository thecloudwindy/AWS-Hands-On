import boto3
from pprint import *

def iam_client():
    iam = boto3.client('iam')
    return iam 

def create_users(user_name):
    response = iam_client().create_user(
        UserName= user_name,
    )
    return response

if __name__ == "__main__":
    number_of_users = int(input("Enter the number of users: "))
    count = 1
    while count <= number_of_users:
        user_name = input("Enter the user name: ")
        result = create_users(user_name)
        pprint(result)
        count += 1