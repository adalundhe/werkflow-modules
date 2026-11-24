from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_dimension_field import QuickSightDimensionField


class QuickSightUniqueValuesComputation(BaseModel):
    ComputationId: StrictStr | None = None
    Name: StrictStr | None = None
    Category: QuickSightDimensionField | None = None
