from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_short_format_text import QuickSightShortFormatText


class QuickSightVisualTitleLabelOptions(BaseModel):
    Visibility: StrictStr | None = None
    FormatText: QuickSightShortFormatText | None = None
