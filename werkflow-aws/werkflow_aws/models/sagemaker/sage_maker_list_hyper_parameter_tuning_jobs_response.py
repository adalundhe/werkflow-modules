from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_hyper_parameter_tuning_job_summary import SageMakerHyperParameterTuningJobSummary


class SageMakerListHyperParameterTuningJobsResponse(BaseModel):
    HyperParameterTuningJobSummaries: list[SageMakerHyperParameterTuningJobSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
