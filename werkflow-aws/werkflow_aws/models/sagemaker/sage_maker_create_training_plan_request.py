from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateTrainingPlanRequest(BaseModel):
    TrainingPlanName: StrictStr
    TrainingPlanOfferingId: StrictStr
    SpareInstanceCountPerUltraServer: StrictInt | None = None
    Tags: list[SageMakerTagModel] | None = None
