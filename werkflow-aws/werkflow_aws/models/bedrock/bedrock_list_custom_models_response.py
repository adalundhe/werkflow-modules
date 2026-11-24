from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_custom_model_summary import BedrockCustomModelSummary


class BedrockListCustomModelsResponse(BaseModel):
    nextToken: StrictStr | None = None
    modelSummaries: list[BedrockCustomModelSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
