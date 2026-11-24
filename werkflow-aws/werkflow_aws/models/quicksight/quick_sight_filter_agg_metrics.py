from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_identifier import QuickSightIdentifier


class QuickSightFilterAggMetrics(BaseModel):
    MetricOperand: QuickSightIdentifier | None = None
    Function: StrictStr | None = None
    SortDirection: StrictStr | None = None
