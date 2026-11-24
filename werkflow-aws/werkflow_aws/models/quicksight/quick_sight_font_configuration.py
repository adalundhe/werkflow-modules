from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_font_size import QuickSightFontSize
from .quick_sight_font_weight import QuickSightFontWeight


class QuickSightFontConfiguration(BaseModel):
    FontSize: QuickSightFontSize | None = None
    FontDecoration: StrictStr | None = None
    FontColor: StrictStr | None = None
    FontWeight: QuickSightFontWeight | None = None
    FontStyle: StrictStr | None = None
    FontFamily: StrictStr | None = None
