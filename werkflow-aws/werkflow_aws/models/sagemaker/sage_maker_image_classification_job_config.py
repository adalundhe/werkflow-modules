from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_auto_ml_job_completion_criteria import SageMakerAutoMLJobCompletionCriteria


class SageMakerImageClassificationJobConfig(BaseModel):
    CompletionCriteria: SageMakerAutoMLJobCompletionCriteria | None = None
