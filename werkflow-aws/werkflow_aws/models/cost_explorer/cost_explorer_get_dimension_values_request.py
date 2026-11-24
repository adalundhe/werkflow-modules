from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dimension import Dimension
from .expression import Expression
from .time_period import TimePeriod as CETimePeriod


class CostExplorerGetDimensionValuesRequest(BaseModel):
    TimePeriod: CETimePeriod
    Dimension: StrictStr
    SearchString: StrictStr | None = None
    Context: StrictStr | None = None
    Filter: Expression | None = None
    SortBy: list[dict[str, StrictStr]] | None = None
    BillingViewArn: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextPageToken: StrictStr | None = None
