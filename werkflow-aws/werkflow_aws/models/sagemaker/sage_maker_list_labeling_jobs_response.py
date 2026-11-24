from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_labeling_job_summary import SageMakerLabelingJobSummary


class SageMakerListLabelingJobsResponse(BaseModel):
    LabelingJobSummaryList: list[SageMakerLabelingJobSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
