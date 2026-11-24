from __future__ import annotations
from pydantic import BaseModel
from .bedrock_model_invocation_job_s3_output_data_config import BedrockModelInvocationJobS3OutputDataConfig


class BedrockModelInvocationJobOutputDataConfig(BaseModel):
    s3OutputDataConfig: BedrockModelInvocationJobS3OutputDataConfig | None = None
