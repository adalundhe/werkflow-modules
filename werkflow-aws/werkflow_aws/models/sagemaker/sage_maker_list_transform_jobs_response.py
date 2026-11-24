from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_transform_job_summary import SageMakerTransformJobSummary


class SageMakerListTransformJobsResponse(BaseModel):
    TransformJobSummaries: list[SageMakerTransformJobSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
