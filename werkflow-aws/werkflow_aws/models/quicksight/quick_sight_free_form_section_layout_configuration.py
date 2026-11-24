from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_free_form_layout_element import QuickSightFreeFormLayoutElement


class QuickSightFreeFormSectionLayoutConfiguration(BaseModel):
    Elements: list[QuickSightFreeFormLayoutElement] | None = None
