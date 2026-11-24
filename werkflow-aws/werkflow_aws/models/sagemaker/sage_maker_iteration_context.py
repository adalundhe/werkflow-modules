from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerIterationContext(BaseModel):
    ParentStepName: StrictStr | None = None
    Index: StrictInt | None = None
    Item: StrictStr | None = None
