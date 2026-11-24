from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_body_section_repeat_dimension_configuration import QuickSightBodySectionRepeatDimensionConfiguration
from .quick_sight_body_section_repeat_page_break_configuration import QuickSightBodySectionRepeatPageBreakConfiguration


class QuickSightBodySectionRepeatConfiguration(BaseModel):
    DimensionConfigurations: list[QuickSightBodySectionRepeatDimensionConfiguration] | None = None
    PageBreakConfiguration: QuickSightBodySectionRepeatPageBreakConfiguration | None = None
    NonRepeatingVisuals: list[StrictStr] | None = None
