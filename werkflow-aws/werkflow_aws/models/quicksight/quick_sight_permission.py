from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightPermission(BaseModel):
    Actions: list[StrictStr] | None = None
    Principal: StrictStr | None = None
