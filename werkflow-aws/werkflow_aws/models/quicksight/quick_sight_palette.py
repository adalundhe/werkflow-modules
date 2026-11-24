from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightPalette(BaseModel):
    Foreground: StrictStr | None = None
    Background: StrictStr | None = None
