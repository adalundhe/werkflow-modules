from __future__ import annotations
from pydantic import BaseModel
from .connect_categories_attribute_filter import ConnectCategoriesAttributeFilter


class ConnectRealTimeContactAnalysisSegmentsFilter(BaseModel):
    CategoriesAttributeFilter: ConnectCategoriesAttributeFilter | None = None
