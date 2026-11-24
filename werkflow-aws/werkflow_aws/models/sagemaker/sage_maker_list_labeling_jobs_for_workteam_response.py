from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_labeling_job_for_workteam_summary import SageMakerLabelingJobForWorkteamSummary


class SageMakerListLabelingJobsForWorkteamResponse(BaseModel):
    LabelingJobSummaryList: list[SageMakerLabelingJobForWorkteamSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
