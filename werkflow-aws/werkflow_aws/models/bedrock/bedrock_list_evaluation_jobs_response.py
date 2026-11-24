from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_evaluation_summary import BedrockEvaluationSummary


class BedrockListEvaluationJobsResponse(BaseModel):
    nextToken: StrictStr | None = None
    jobSummaries: list[BedrockEvaluationSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
