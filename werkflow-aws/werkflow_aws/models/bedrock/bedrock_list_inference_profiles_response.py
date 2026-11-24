from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_inference_profile_summary import BedrockInferenceProfileSummary


class BedrockListInferenceProfilesResponse(BaseModel):
    inferenceProfileSummaries: list[BedrockInferenceProfileSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
