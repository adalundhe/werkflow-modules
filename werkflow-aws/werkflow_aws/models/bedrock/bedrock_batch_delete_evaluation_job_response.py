from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .bedrock_batch_delete_evaluation_job_error import BedrockBatchDeleteEvaluationJobError
from .bedrock_batch_delete_evaluation_job_item import BedrockBatchDeleteEvaluationJobItem


class BedrockBatchDeleteEvaluationJobResponse(BaseModel):
    errors: list[BedrockBatchDeleteEvaluationJobError] | None = None
    evaluationJobs: list[BedrockBatchDeleteEvaluationJobItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
