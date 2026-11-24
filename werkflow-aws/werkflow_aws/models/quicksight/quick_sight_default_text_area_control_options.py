from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_text_area_control_display_options import QuickSightTextAreaControlDisplayOptions


class QuickSightDefaultTextAreaControlOptions(BaseModel):
    Delimiter: StrictStr | None = None
    DisplayOptions: QuickSightTextAreaControlDisplayOptions | None = None
