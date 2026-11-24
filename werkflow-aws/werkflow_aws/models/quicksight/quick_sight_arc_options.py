from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightArcOptions(BaseModel):
    ArcThickness: StrictStr | None = None
