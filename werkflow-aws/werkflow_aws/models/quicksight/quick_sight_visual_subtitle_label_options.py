from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_long_format_text import QuickSightLongFormatText


class QuickSightVisualSubtitleLabelOptions(BaseModel):
    Visibility: StrictStr | None = None
    FormatText: QuickSightLongFormatText | None = None
