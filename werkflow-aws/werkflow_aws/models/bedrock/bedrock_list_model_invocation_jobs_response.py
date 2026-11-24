from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_model_invocation_job_summary import BedrockModelInvocationJobSummary


class BedrockListModelInvocationJobsResponse(BaseModel):
    nextToken: StrictStr | None = None
    invocationJobSummaries: list[BedrockModelInvocationJobSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
