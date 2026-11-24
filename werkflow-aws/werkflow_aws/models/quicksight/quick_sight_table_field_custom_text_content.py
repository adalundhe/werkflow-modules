from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_font_configuration import QuickSightFontConfiguration


class QuickSightTableFieldCustomTextContent(BaseModel):
    Value: StrictStr | None = None
    FontConfiguration: QuickSightFontConfiguration | None = None
