from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightNumericEqualityDrillDownFilter(BaseModel):
    Column: QuickSightColumnIdentifier | None = None
    Value: StrictFloat | StrictInt | None = None
