from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_section_layout_configuration import QuickSightSectionLayoutConfiguration
from .quick_sight_section_style import QuickSightSectionStyle


class QuickSightHeaderFooterSectionConfiguration(BaseModel):
    SectionId: StrictStr | None = None
    Layout: QuickSightSectionLayoutConfiguration | None = None
    Style: QuickSightSectionStyle | None = None
