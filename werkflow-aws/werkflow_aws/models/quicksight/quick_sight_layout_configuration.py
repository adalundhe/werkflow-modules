from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_free_form_layout_configuration import QuickSightFreeFormLayoutConfiguration
from .quick_sight_grid_layout_configuration import QuickSightGridLayoutConfiguration
from .quick_sight_section_based_layout_configuration import QuickSightSectionBasedLayoutConfiguration


class QuickSightLayoutConfiguration(BaseModel):
    GridLayout: QuickSightGridLayoutConfiguration | None = None
    FreeFormLayout: QuickSightFreeFormLayoutConfiguration | None = None
    SectionBasedLayout: QuickSightSectionBasedLayoutConfiguration | None = None
