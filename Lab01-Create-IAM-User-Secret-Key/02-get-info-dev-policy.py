import boto3
from pprint import *

# Create IAM client
def iam_client():
    iam = boto3.client('iam')
    return iam

# Get a policy
def get_info_policy(arn):
    response = iam_client().get_policy(
        PolicyArn = arn
    )
    return(response['Policy'])

if __name__ == "__main__":
    arn = input("Enter the ARN of policy: ")
    result = get_info_policy(arn)
    pprint(result)
    