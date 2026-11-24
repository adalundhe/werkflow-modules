from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_advanced_prompt_optimization_job_summary import BedrockAdvancedPromptOptimizationJobSummary


class BedrockListAdvancedPromptOptimizationJobsResponse(BaseModel):
    jobSummaries: list[BedrockAdvancedPromptOptimizationJobSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
