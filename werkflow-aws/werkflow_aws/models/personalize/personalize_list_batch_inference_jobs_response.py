from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_batch_inference_job_summary import PersonalizeBatchInferenceJobSummary


class PersonalizeListBatchInferenceJobsResponse(BaseModel):
    batchInferenceJobs: list[PersonalizeBatchInferenceJobSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
