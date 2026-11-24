from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightFreeFormLayoutElementBackgroundStyle(BaseModel):
    Visibility: StrictStr | None = None
    Color: StrictStr | None = None
