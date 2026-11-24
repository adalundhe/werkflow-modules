from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_section_after_page_break import QuickSightSectionAfterPageBreak


class QuickSightBodySectionRepeatPageBreakConfiguration(BaseModel):
    After: QuickSightSectionAfterPageBreak | None = None
