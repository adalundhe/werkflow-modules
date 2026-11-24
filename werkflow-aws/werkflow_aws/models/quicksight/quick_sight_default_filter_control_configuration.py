from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_control_title_format_text import QuickSightControlTitleFormatText
from .quick_sight_default_filter_control_options import QuickSightDefaultFilterControlOptions


class QuickSightDefaultFilterControlConfiguration(BaseModel):
    Title: StrictStr | None = None
    ControlOptions: QuickSightDefaultFilterControlOptions | None = None
    ControlTitleFormatText: QuickSightControlTitleFormatText | None = None
