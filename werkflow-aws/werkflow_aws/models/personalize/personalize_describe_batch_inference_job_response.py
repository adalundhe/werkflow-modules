from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_batch_inference_job import PersonalizeBatchInferenceJob


class PersonalizeDescribeBatchInferenceJobResponse(BaseModel):
    batchInferenceJob: PersonalizeBatchInferenceJob | None = None
    ResponseMetadata: dict[str, Any] | None = None
