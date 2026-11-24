from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_batch_segment_job import PersonalizeBatchSegmentJob


class PersonalizeDescribeBatchSegmentJobResponse(BaseModel):
    batchSegmentJob: PersonalizeBatchSegmentJob | None = None
    ResponseMetadata: dict[str, Any] | None = None
