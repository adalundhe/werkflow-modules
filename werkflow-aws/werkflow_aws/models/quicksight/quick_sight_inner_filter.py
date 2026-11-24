from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_category_inner_filter import QuickSightCategoryInnerFilter


class QuickSightInnerFilter(BaseModel):
    CategoryInnerFilter: QuickSightCategoryInnerFilter | None = None
