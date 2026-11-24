from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerLabelingJobStoppingConditions(BaseModel):
    MaxHumanLabeledObjectCount: StrictInt | None = None
    MaxPercentageOfInputDatasetLabeled: StrictInt | None = None
