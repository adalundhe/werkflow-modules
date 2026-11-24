from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2TargetGroupTuple(BaseModel):
    TargetGroupArn: StrictStr | None = None
    Weight: StrictInt | None = None
