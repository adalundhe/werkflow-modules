from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sage_maker_training_plan_extension import SageMakerTrainingPlanExtension


class SageMakerExtendTrainingPlanResponse(BaseModel):
    TrainingPlanExtensions: list[SageMakerTrainingPlanExtension] | None = None
    ResponseMetadata: dict[str, Any] | None = None
