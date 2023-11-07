from aws_cdk import (
    Stack,
    aws_s3 as s3
)
from constructs import Construct

class BaCloudAcademyGithubCdkAndrzejStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(
            self, 
            'bucket-object', # this is just the CDK object name
            bucket_name='ba-github-cdk-bucket-andrzej'
        )
