from __future__ import annotations
from pydantic import BaseModel
from .bedrock_lambda_grader_config import BedrockLambdaGraderConfig


class BedrockGraderConfig(BaseModel):
    lambdaGrader: BedrockLambdaGraderConfig | None = None
