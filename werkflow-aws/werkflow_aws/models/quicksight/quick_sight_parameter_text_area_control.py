from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_control_title_format_text import QuickSightControlTitleFormatText
from .quick_sight_text_area_control_display_options import QuickSightTextAreaControlDisplayOptions


class QuickSightParameterTextAreaControl(BaseModel):
    ParameterControlId: StrictStr | None = None
    Title: StrictStr | None = None
    SourceParameterName: StrictStr | None = None
    Delimiter: StrictStr | None = None
    DisplayOptions: QuickSightTextAreaControlDisplayOptions | None = None
    ControlTitleFormatText: QuickSightControlTitleFormatText | None = None
