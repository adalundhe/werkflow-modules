from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightVisualOptions(BaseModel):
    type: StrictStr | None = None
