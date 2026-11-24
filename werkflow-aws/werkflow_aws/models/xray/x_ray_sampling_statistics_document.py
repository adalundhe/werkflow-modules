from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class XRaySamplingStatisticsDocument(BaseModel):
    RuleName: StrictStr
    ClientID: StrictStr
    Timestamp: datetime.datetime | StrictStr
    RequestCount: StrictInt
    SampledCount: StrictInt
    BorrowCount: StrictInt | None = None
