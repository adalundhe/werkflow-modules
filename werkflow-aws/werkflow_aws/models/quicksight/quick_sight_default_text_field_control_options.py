from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_text_field_control_display_options import QuickSightTextFieldControlDisplayOptions


class QuickSightDefaultTextFieldControlOptions(BaseModel):
    DisplayOptions: QuickSightTextFieldControlDisplayOptions | None = None
