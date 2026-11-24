from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EMRModifyClusterRequest(BaseModel):
    ClusterId: StrictStr
    StepConcurrencyLevel: StrictInt | None = None
    ExtendedSupport: StrictBool | None = None
