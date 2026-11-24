from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightTableBorderOptions(BaseModel):
    Color: StrictStr | None = None
    Thickness: StrictInt | None = None
    Style: StrictStr | None = None
