from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SESGetDomainStatisticsReportRequest(BaseModel):
    Domain: StrictStr
    StartDate: datetime.datetime | StrictStr
    EndDate: datetime.datetime | StrictStr
