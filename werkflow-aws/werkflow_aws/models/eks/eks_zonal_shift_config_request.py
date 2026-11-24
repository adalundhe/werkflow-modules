from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EKSZonalShiftConfigRequest(BaseModel):
    enabled: StrictBool | None = None
