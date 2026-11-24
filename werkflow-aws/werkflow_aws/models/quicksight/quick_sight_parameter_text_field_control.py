from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_control_title_format_text import QuickSightControlTitleFormatText
from .quick_sight_text_field_control_display_options import QuickSightTextFieldControlDisplayOptions


class QuickSightParameterTextFieldControl(BaseModel):
    ParameterControlId: StrictStr | None = None
    Title: StrictStr | None = None
    SourceParameterName: StrictStr | None = None
    DisplayOptions: QuickSightTextFieldControlDisplayOptions | None = None
    ControlTitleFormatText: QuickSightControlTitleFormatText | None = None
