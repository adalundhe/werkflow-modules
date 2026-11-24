from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .expression import Expression
from .time_period import TimePeriod as CETimePeriod


class CostExplorerGetTagsRequest(BaseModel):
    TimePeriod: CETimePeriod
    SearchString: StrictStr | None = None
    TagKey: StrictStr | None = None
    Filter: Expression | None = None
    SortBy: list[dict[str, StrictStr]] | None = None
    BillingViewArn: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextPageToken: StrictStr | None = None
