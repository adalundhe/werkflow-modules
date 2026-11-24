from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_display_format_options import QuickSightDisplayFormatOptions


class QuickSightDefaultFormatting(BaseModel):
    DisplayFormat: StrictStr | None = None
    DisplayFormatOptions: QuickSightDisplayFormatOptions | None = None
