from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_body_section_content import QuickSightBodySectionContent
from .quick_sight_body_section_repeat_configuration import QuickSightBodySectionRepeatConfiguration
from .quick_sight_section_page_break_configuration import QuickSightSectionPageBreakConfiguration
from .quick_sight_section_style import QuickSightSectionStyle


class QuickSightBodySectionConfiguration(BaseModel):
    SectionId: StrictStr | None = None
    Content: QuickSightBodySectionContent | None = None
    Style: QuickSightSectionStyle | None = None
    PageBreakConfiguration: QuickSightSectionPageBreakConfiguration | None = None
    RepeatConfiguration: QuickSightBodySectionRepeatConfiguration | None = None
