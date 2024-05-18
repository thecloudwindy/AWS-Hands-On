# Create Policy with full permissions of services: S3, DynamDB, CodeCommit, CodeBuild, CodeDeploy, CodePipeline
import json
import boto3
from pprint import *

def iam_client():
    iam = boto3.client('iam')
    return iam

def create_policy():
    dev_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "s3:*",
                "Resource": [
                    "*",
                    "*"
                ]
            },
            {
                "Sid": "Statement1",
                "Effect": "Allow",
                "Action": [
                    "dynamodb:*"
                ],
                "Resource": [
                    "*"
                ]
            },
            {
                "Sid": "Statement2",
                "Effect": "Allow",
                "Action": [
                    "codecommit:*"
                ],
                "Resource": [
                    "*",
                    "*"
                ]
            },
            {
                "Sid": "Statement3",
                "Effect": "Allow",
                "Action": [
                    "codebuild:*"
                ],
                "Resource": [
                    "*"
                ]
            },
            {
                "Sid": "Statement4",
                "Effect": "Allow",
                "Action": [
                    "codedeploy:*"
                ],
                "Resource": [
                    "*"
                ]
            },
            {
                "Sid": "Statement5",
                "Effect": "Allow",
                "Action": [
                    "codepipeline:*"
                ],
                "Resource": [
                    "*"
                ]
            }
        ]
    }

    response = iam_client().create_policy(
    PolicyName='DevPolicy',
    PolicyDocument=json.dumps(dev_policy)
    )

    return response

if __name__ == "__main__":
    pprint(create_policy())

    