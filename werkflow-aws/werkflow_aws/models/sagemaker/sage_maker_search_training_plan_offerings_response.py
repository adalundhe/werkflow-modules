from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sage_maker_training_plan_extension_offering import SageMakerTrainingPlanExtensionOffering
from .sage_maker_training_plan_offering import SageMakerTrainingPlanOffering


class SageMakerSearchTrainingPlanOfferingsResponse(BaseModel):
    TrainingPlanOfferings: list[SageMakerTrainingPlanOffering] | None = None
    TrainingPlanExtensionOfferings: list[SageMakerTrainingPlanExtensionOffering] | None = None
    ResponseMetadata: dict[str, Any] | None = None
