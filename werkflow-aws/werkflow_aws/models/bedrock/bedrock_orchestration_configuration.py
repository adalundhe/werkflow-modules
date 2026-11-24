from __future__ import annotations
from pydantic import BaseModel
from .bedrock_query_transformation_configuration import BedrockQueryTransformationConfiguration


class BedrockOrchestrationConfiguration(BaseModel):
    queryTransformationConfiguration: BedrockQueryTransformationConfiguration | None = None
