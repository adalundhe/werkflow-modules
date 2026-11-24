from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightBorderSettings(BaseModel):
    BorderVisibility: StrictStr | None = None
    BorderWidth: StrictStr | None = None
    BorderColor: StrictStr | None = None
