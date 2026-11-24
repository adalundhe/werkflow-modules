from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EKSLogSetupModel(BaseModel):
    types: list[StrictStr] | None = None
    enabled: StrictBool | None = None
