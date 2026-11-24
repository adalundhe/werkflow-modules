from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_free_form_section_layout_configuration import QuickSightFreeFormSectionLayoutConfiguration


class QuickSightSectionLayoutConfiguration(BaseModel):
    FreeFormLayout: QuickSightFreeFormSectionLayoutConfiguration | None = None
