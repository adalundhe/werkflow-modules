from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightProgressBarOptions(BaseModel):
    Visibility: StrictStr | None = None
