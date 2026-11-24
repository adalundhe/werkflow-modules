from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerIntegerParameterRange(BaseModel):
    Name: StrictStr | None = None
    MinValue: StrictStr | None = None
    MaxValue: StrictStr | None = None
    ScalingType: StrictStr | None = None
