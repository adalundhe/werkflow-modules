from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .bedrock_foundation_model_summary import BedrockFoundationModelSummary


class BedrockListFoundationModelsResponse(BaseModel):
    modelSummaries: list[BedrockFoundationModelSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
