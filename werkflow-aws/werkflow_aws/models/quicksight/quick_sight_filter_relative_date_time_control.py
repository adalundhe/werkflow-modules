from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_control_title_format_text import QuickSightControlTitleFormatText
from .quick_sight_relative_date_time_control_display_options import QuickSightRelativeDateTimeControlDisplayOptions


class QuickSightFilterRelativeDateTimeControl(BaseModel):
    FilterControlId: StrictStr | None = None
    Title: StrictStr | None = None
    SourceFilterId: StrictStr | None = None
    DisplayOptions: QuickSightRelativeDateTimeControlDisplayOptions | None = None
    CommitMode: StrictStr | None = None
    ControlTitleFormatText: QuickSightControlTitleFormatText | None = None
