from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightParameterSelectableValues(BaseModel):
    Values: list[StrictStr] | None = None
    LinkToDataSetColumn: QuickSightColumnIdentifier | None = None
