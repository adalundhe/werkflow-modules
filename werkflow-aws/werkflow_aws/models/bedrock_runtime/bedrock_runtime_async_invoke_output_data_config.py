from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_async_invoke_s3_output_data_config import BedrockRuntimeAsyncInvokeS3OutputDataConfig


class BedrockRuntimeAsyncInvokeOutputDataConfig(BaseModel):
    s3OutputDataConfig: BedrockRuntimeAsyncInvokeS3OutputDataConfig | None = None
