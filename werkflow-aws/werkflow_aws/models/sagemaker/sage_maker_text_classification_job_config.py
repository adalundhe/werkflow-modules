from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_auto_ml_job_completion_criteria import SageMakerAutoMLJobCompletionCriteria


class SageMakerTextClassificationJobConfig(BaseModel):
    CompletionCriteria: SageMakerAutoMLJobCompletionCriteria | None = None
    ContentColumn: StrictStr | None = None
    TargetLabelColumn: StrictStr | None = None
