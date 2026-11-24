from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightTopBottomMoversComputation(BaseModel):
    ComputationId: StrictStr | None = None
    Name: StrictStr | None = None
    Time: QuickSightDimensionField | None = None
    Category: QuickSightDimensionField | None = None
    Value: QuickSightMeasureField | None = None
    MoverSize: StrictInt | None = None
    SortOrder: StrictStr | None = None
    Type: StrictStr | None = None
