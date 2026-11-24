from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EKSResourceWeight(BaseModel):
    name: StrictStr | None = None
    weight: StrictInt | None = None
