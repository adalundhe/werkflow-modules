from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightFreeFormLayoutElementBorderStyle(BaseModel):
    Visibility: StrictStr | None = None
    Color: StrictStr | None = None
    Width: StrictStr | None = None
