from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_imported_model_summary import BedrockImportedModelSummary


class BedrockListImportedModelsResponse(BaseModel):
    nextToken: StrictStr | None = None
    modelSummaries: list[BedrockImportedModelSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
