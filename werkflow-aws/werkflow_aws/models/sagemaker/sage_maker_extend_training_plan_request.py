from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerExtendTrainingPlanRequest(BaseModel):
    TrainingPlanExtensionOfferingId: StrictStr
