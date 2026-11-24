from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightBorderStyle(BaseModel):
    Color: StrictStr | None = None
    Show: StrictBool | None = None
    Width: StrictStr | None = None
