from __future__ import annotations
from pydantic import BaseModel
from .bedrock_model_package_arn_data_source import BedrockModelPackageArnDataSource


class BedrockCustomModelDataSource(BaseModel):
    modelPackageArnDataSource: BedrockModelPackageArnDataSource | None = None
