from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class XRaySamplingStatisticSummary(BaseModel):
    RuleName: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
    RequestCount: StrictInt | None = None
    BorrowCount: StrictInt | None = None
    SampledCount: StrictInt | None = None
