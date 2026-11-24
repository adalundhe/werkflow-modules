from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_section_layout_configuration import QuickSightSectionLayoutConfiguration


class QuickSightBodySectionContent(BaseModel):
    Layout: QuickSightSectionLayoutConfiguration | None = None
