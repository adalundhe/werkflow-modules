from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_unaggregated_field import QuickSightUnaggregatedField


class QuickSightTableUnaggregatedFieldWells(BaseModel):
    Values: list[QuickSightUnaggregatedField] | None = None
