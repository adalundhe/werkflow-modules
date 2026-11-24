from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightResourcePermission(BaseModel):
    Principal: StrictStr | None = None
    Actions: list[StrictStr] | None = None
