from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTableStyleTarget(BaseModel):
    CellType: StrictStr | None = None
