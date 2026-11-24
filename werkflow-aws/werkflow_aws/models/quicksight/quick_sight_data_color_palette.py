from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataColorPalette(BaseModel):
    Colors: list[StrictStr] | None = None
    MinMaxGradient: list[StrictStr] | None = None
    EmptyFillColor: StrictStr | None = None
