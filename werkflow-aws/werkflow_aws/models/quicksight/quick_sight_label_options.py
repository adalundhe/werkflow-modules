from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_font_configuration import QuickSightFontConfiguration


class QuickSightLabelOptions(BaseModel):
    Visibility: StrictStr | None = None
    FontConfiguration: QuickSightFontConfiguration | None = None
    CustomLabel: StrictStr | None = None
