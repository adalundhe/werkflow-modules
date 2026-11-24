from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerContinuousParameterRangeSpecification(BaseModel):
    MinValue: StrictStr | None = None
    MaxValue: StrictStr | None = None
