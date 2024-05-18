import boto3
from pprint import *

def codecommit_client():
    client = boto3.client('codecommit')
    return client

def get_repo(repositoryName):
    response = codecommit_client().get_repository(
        repositoryName=repositoryName
    )
    return response

if __name__ == "__main__":
    repositoryName = input("Enter the name of repository: ")
    result = get_repo(repositoryName)
    pprint(result)

