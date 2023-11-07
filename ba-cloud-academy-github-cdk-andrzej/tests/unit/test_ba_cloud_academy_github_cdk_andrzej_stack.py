import aws_cdk as core
import aws_cdk.assertions as assertions

from ba_cloud_academy_github_cdk_andrzej.ba_cloud_academy_github_cdk_andrzej_stack import BaCloudAcademyGithubCdkAndrzejStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ba_cloud_academy_github_cdk_andrzej/ba_cloud_academy_github_cdk_andrzej_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BaCloudAcademyGithubCdkAndrzejStack(app, "ba-cloud-academy-github-cdk-andrzej")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
