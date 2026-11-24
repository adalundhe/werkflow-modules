from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_training_job_summary import SageMakerTrainingJobSummary


class SageMakerListTrainingJobsResponse(BaseModel):
    TrainingJobSummaries: list[SageMakerTrainingJobSummary] | None = None
    NextToken: StrictStr | None = None
