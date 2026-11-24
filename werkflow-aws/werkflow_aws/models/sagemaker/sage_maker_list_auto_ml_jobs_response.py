from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_auto_ml_job_summary import SageMakerAutoMLJobSummary


class SageMakerListAutoMLJobsResponse(BaseModel):
    AutoMLJobSummaries: list[SageMakerAutoMLJobSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
