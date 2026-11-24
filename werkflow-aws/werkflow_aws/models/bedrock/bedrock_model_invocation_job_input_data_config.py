from __future__ import annotations
from pydantic import BaseModel
from .bedrock_model_invocation_job_s3_input_data_config import BedrockModelInvocationJobS3InputDataConfig


class BedrockModelInvocationJobInputDataConfig(BaseModel):
    s3InputDataConfig: BedrockModelInvocationJobS3InputDataConfig | None = None
