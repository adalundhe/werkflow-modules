from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDonutCenterOptions(BaseModel):
    LabelVisibility: StrictStr | None = None
