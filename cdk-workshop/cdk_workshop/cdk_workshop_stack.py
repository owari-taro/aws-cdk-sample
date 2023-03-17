from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)


class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Defines an AWS Lambda resource
        #my_lambda = _lambda.Function(
        #    self, 'HelloHandler',
        #    runtime=_lambda.Runtime.PYTHON_3_9,
        #    code=_lambda.Code.from_asset('lambda'),
        #    handler='hello.handler',
        #)
        code=_lambda.DockerImageCode.from_image_asset(
                # Directory relative to where you execute cdk deploy  contains a Dockerfile with build instructions
                "lambda/"
            )
        my_lambda = _lambda.DockerImageFunction(
            self, "ExampleDockerLambda",
            # Function name on AWS
            function_name="ExampleDockerLambda",
            # Use aws_cdk.aws_lambda.DockerImageCode.from_image_asset to build
            # a docker image on deployment
            code=code)



'''
            id="ExampleDockerLambda",
            # Function name on AWS
            function_name="ExampleDockerLambda",
            # Use aws_cdk.aws_lambda.DockerImageCode.from_image_asset to build
            # a docker image on deployment
            code=_lambda.DockerImageCode.from_image_asset(
                # Directory relative to where you execute cdk deploy
                # contains a Dockerfile with build instructions
                directory="cdk_docker_lambda/ExampleDockerLambda"
            ),
'''