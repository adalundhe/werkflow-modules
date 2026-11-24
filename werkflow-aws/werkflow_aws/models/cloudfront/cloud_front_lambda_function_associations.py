from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_lambda_function_association import CloudFrontLambdaFunctionAssociation


class CloudFrontLambdaFunctionAssociations(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[CloudFrontLambdaFunctionAssociation] | None = None
