from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_training_plan_summary import SageMakerTrainingPlanSummary


class SageMakerListTrainingPlansResponse(BaseModel):
    NextToken: StrictStr | None = None
    TrainingPlanSummaries: list[SageMakerTrainingPlanSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
