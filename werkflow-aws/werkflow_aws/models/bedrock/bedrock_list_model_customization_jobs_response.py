from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_model_customization_job_summary import BedrockModelCustomizationJobSummary


class BedrockListModelCustomizationJobsResponse(BaseModel):
    nextToken: StrictStr | None = None
    modelCustomizationJobSummaries: list[BedrockModelCustomizationJobSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
