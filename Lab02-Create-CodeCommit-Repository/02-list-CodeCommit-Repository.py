import boto3
from pprint import *

def codecommit_client():
    client = boto3.client('codecommit')
    return client

def list_repositories():
    response = codecommit_client().list_repositories(
        sortBy='repositoryName'
    )
    return response 

if __name__ == "__main__":
    result = list_repositories()
    for repo in result['repositories']:
        pprint(repo['repositoryName'])