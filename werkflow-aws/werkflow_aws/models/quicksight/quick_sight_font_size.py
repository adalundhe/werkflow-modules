from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightFontSize(BaseModel):
    Relative: StrictStr | None = None
    Absolute: StrictStr | None = None
