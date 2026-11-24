from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes
from .bedrock_runtime_s3_location import BedrockRuntimeS3Location


class BedrockRuntimeVideoSource(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    bytes: StrictBytes | Any | None = None
    s3Location: BedrockRuntimeS3Location | None = None
