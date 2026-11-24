from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTablePinnedFieldOptions(BaseModel):
    PinnedLeftFields: list[StrictStr] | None = None
