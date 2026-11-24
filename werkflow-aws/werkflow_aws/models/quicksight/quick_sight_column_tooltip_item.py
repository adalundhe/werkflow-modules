from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_aggregation_function import QuickSightAggregationFunction
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightColumnTooltipItem(BaseModel):
    Column: QuickSightColumnIdentifier | None = None
    Label: StrictStr | None = None
    Visibility: StrictStr | None = None
    Aggregation: QuickSightAggregationFunction | None = None
    TooltipTarget: StrictStr | None = None
