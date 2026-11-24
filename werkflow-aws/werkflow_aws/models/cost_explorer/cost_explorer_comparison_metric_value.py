from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerComparisonMetricValue(BaseModel):
    BaselineTimePeriodAmount: StrictStr | None = None
    ComparisonTimePeriodAmount: StrictStr | None = None
    Difference: StrictStr | None = None
    Unit: StrictStr | None = None
