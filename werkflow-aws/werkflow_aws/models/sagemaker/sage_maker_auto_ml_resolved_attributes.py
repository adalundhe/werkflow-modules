from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_auto_ml_job_completion_criteria import SageMakerAutoMLJobCompletionCriteria
from .sage_maker_auto_ml_job_objective import SageMakerAutoMLJobObjective
from .sage_maker_auto_ml_problem_type_resolved_attributes import SageMakerAutoMLProblemTypeResolvedAttributes


class SageMakerAutoMLResolvedAttributes(BaseModel):
    AutoMLJobObjective: SageMakerAutoMLJobObjective | None = None
    CompletionCriteria: SageMakerAutoMLJobCompletionCriteria | None = None
    AutoMLProblemTypeResolvedAttributes: SageMakerAutoMLProblemTypeResolvedAttributes | None = None
