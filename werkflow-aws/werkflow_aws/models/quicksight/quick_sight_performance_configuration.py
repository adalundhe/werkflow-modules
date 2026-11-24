from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_unique_key import QuickSightUniqueKey


class QuickSightPerformanceConfiguration(BaseModel):
    UniqueKeys: list[QuickSightUniqueKey] | None = None
