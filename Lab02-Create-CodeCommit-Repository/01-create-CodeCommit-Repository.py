import boto3
from pprint import *

def codecommit_client():
    client = boto3.client('codecommit')
    return client

def create_repository(repositoryName):
    response = codecommit_client().create_repository(
        repositoryName=repositoryName,
    )
    return response

if __name__ == "__main__":
    repositoryName = input("Enter the repository name: ")
    result = create_repository(repositoryName)
    pprint(result)

