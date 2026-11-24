from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .bedrock_foundation_model_details import BedrockFoundationModelDetails


class BedrockGetFoundationModelResponse(BaseModel):
    modelDetails: BedrockFoundationModelDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
