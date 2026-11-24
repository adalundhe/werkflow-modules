from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightMaximumLabelType(BaseModel):
    Visibility: StrictStr | None = None
