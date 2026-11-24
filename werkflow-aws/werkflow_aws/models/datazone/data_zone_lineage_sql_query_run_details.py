from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneLineageSqlQueryRunDetails(BaseModel):
    queryStartTime: datetime.datetime | StrictStr | None = None
    queryEndTime: datetime.datetime | StrictStr | None = None
    totalQueriesProcessed: StrictInt | None = None
    numQueriesFailed: StrictInt | None = None
    errorMessages: list[StrictStr] | None = None
