from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerModelLatencyThreshold(BaseModel):
    Percentile: StrictStr | None = None
    ValueInMilliseconds: StrictInt | None = None
