from __future__ import annotations
from pydantic import BaseModel
from .bedrock_s3_data_source import BedrockS3DataSource


class BedrockModelDataSource(BaseModel):
    s3DataSource: BedrockS3DataSource | None = None
