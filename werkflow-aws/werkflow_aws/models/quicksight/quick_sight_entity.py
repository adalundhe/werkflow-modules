from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightEntity(BaseModel):
    Path: StrictStr | None = None
