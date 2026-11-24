from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerLabelingJobDataAttributes(BaseModel):
    ContentClassifiers: list[StrictStr] | None = None
