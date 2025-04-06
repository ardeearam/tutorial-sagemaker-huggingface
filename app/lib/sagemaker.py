import json
import boto3
from django.conf import settings


class SageMakerRuntime:
    def __init__(self):
      self.client = boto3.client("sagemaker-runtime")

    def invoke_endpoint(self, payload):
      endpoint_name = settings.SAGEMAKER_ENDPOINT_NAME
      response = self.client.invoke_endpoint(
          EndpointName=endpoint_name,
          ContentType="application/json",
          Body=json.dumps(payload)
      )

      return response["Body"].read().decode()


