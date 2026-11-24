from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class WAFv2DataPointEntry(BaseModel):
    Date: datetime.datetime | StrictStr | None = None
    MonetizeServedCount: StrictInt | None = None
    SettledCount: StrictInt | None = None
    TotalAmount: StrictStr | None = None
    Category: StrictStr | None = None
    Intent: StrictStr | None = None
    GroupByValue: StrictStr | None = None
