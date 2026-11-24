from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_control_title_format_text import QuickSightControlTitleFormatText
from .quick_sight_date_time_picker_control_display_options import QuickSightDateTimePickerControlDisplayOptions


class QuickSightParameterDateTimePickerControl(BaseModel):
    ParameterControlId: StrictStr | None = None
    Title: StrictStr | None = None
    SourceParameterName: StrictStr | None = None
    DisplayOptions: QuickSightDateTimePickerControlDisplayOptions | None = None
    ControlTitleFormatText: QuickSightControlTitleFormatText | None = None
