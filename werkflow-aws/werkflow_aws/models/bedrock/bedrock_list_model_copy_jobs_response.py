from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_model_copy_job_summary import BedrockModelCopyJobSummary


class BedrockListModelCopyJobsResponse(BaseModel):
    nextToken: StrictStr | None = None
    modelCopyJobSummaries: list[BedrockModelCopyJobSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
