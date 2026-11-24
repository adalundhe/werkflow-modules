from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightMinimumLabelType(BaseModel):
    Visibility: StrictStr | None = None
