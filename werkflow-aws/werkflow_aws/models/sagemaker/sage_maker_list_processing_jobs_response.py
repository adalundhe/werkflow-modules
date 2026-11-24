from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_processing_job_summary import SageMakerProcessingJobSummary


class SageMakerListProcessingJobsResponse(BaseModel):
    ProcessingJobSummaries: list[SageMakerProcessingJobSummary] | None = None
    NextToken: StrictStr | None = None
