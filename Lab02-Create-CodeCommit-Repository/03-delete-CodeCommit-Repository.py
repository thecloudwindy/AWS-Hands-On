import boto3
from pprint import *

def codecommit_client():
    client = boto3.client('codecommit')
    return client

def delete_repo(repositoryName):
    response = codecommit_client().delete_repository(
        repositoryName= repositoryName
    )
    return response

if __name__ == "__main__":
    repositoryName = input("Enter the name of repository: ")
    result = delete_repo(repositoryName)
    pprint(result)

