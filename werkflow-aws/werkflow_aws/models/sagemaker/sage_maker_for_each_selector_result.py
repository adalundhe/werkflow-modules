from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerForEachSelectorResult(BaseModel):
    StepName: StrictStr | None = None
    Index: StrictInt | None = None
