from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_model_import_job_summary import BedrockModelImportJobSummary


class BedrockListModelImportJobsResponse(BaseModel):
    nextToken: StrictStr | None = None
    modelImportJobSummaries: list[BedrockModelImportJobSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
