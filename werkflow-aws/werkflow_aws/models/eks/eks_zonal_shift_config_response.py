from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EKSZonalShiftConfigResponse(BaseModel):
    enabled: StrictBool | None = None
