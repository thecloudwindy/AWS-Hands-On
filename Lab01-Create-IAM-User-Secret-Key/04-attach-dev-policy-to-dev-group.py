import boto3 
from pprint import * 

def iam_client():
    iam = boto3.client('iam')
    return iam 

def attach_policy_to_group(group_name, policy_arn):
    response = iam_client().attach_group_policy(
        GroupName= group_name,
        PolicyArn= policy_arn
    )
    return response 

if __name__ == "__main__":
    group_name = 'dev-group'
    policy_arn = 'arn:aws:iam::994823578500:policy/DevPolicy'
    result = attach_policy_to_group(group_name, policy_arn)
    pprint(result)

