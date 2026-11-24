from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightFieldFolder(BaseModel):
    description: StrictStr | None = None
    columns: list[StrictStr] | None = None
