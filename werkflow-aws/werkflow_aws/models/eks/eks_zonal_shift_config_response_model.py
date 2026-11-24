from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EKSZonalShiftConfigResponseModel(BaseModel):
    enabled: StrictBool | None = None
