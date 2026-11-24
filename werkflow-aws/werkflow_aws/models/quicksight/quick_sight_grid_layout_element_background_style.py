from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGridLayoutElementBackgroundStyle(BaseModel):
    Visibility: StrictStr | None = None
    Color: StrictStr | None = None
