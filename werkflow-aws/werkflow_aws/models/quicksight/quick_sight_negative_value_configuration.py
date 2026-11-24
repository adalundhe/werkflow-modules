from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightNegativeValueConfiguration(BaseModel):
    DisplayMode: StrictStr | None = None
