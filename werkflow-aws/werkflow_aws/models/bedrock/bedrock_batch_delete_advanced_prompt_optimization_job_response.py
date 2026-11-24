from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .bedrock_batch_delete_advanced_prompt_optimization_job_error import BedrockBatchDeleteAdvancedPromptOptimizationJobError
from .bedrock_batch_delete_advanced_prompt_optimization_job_item import BedrockBatchDeleteAdvancedPromptOptimizationJobItem


class BedrockBatchDeleteAdvancedPromptOptimizationJobResponse(BaseModel):
    errors: list[BedrockBatchDeleteAdvancedPromptOptimizationJobError] | None = None
    advancedPromptOptimizationJobs: list[BedrockBatchDeleteAdvancedPromptOptimizationJobItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
