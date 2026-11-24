from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_font_configuration import QuickSightFontConfiguration


class QuickSightControlTitleFontConfiguration(BaseModel):
    FontConfiguration: QuickSightFontConfiguration | None = None
    TextAlignment: StrictStr | None = None
