from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_auto_ml_job_completion_criteria import SageMakerAutoMLJobCompletionCriteria
from .sage_maker_auto_ml_job_objective import SageMakerAutoMLJobObjective


class SageMakerResolvedAttributes(BaseModel):
    AutoMLJobObjective: SageMakerAutoMLJobObjective | None = None
    ProblemType: StrictStr | None = None
    CompletionCriteria: SageMakerAutoMLJobCompletionCriteria | None = None
