from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_date_time_picker_control_display_options import QuickSightDateTimePickerControlDisplayOptions


class QuickSightDefaultDateTimePickerControlOptions(BaseModel):
    Type: StrictStr | None = None
    DisplayOptions: QuickSightDateTimePickerControlDisplayOptions | None = None
    CommitMode: StrictStr | None = None
