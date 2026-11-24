from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_batch_segment_job_summary import PersonalizeBatchSegmentJobSummary


class PersonalizeListBatchSegmentJobsResponse(BaseModel):
    batchSegmentJobs: list[PersonalizeBatchSegmentJobSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
