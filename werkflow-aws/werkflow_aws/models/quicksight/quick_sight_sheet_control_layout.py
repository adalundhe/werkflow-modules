from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_sheet_control_layout_configuration import QuickSightSheetControlLayoutConfiguration


class QuickSightSheetControlLayout(BaseModel):
    Configuration: QuickSightSheetControlLayoutConfiguration | None = None
