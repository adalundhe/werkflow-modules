from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGovernance(BaseModel):
    DefaultCategoryEffects: dict[StrictStr, StrictStr] | None = None
