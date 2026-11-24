from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_relative_date_time_control_display_options import QuickSightRelativeDateTimeControlDisplayOptions


class QuickSightDefaultRelativeDateTimeControlOptions(BaseModel):
    DisplayOptions: QuickSightRelativeDateTimeControlDisplayOptions | None = None
    CommitMode: StrictStr | None = None
