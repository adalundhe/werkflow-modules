from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_spacing import QuickSightSpacing


class QuickSightSectionStyle(BaseModel):
    Height: StrictStr | None = None
    Padding: QuickSightSpacing | None = None
