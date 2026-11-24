from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerTtlDuration(BaseModel):
    Unit: StrictStr | None = None
    Value: StrictInt | None = None
