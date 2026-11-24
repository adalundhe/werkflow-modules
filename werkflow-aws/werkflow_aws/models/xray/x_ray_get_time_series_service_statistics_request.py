from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class XRayGetTimeSeriesServiceStatisticsRequest(BaseModel):
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
    GroupName: StrictStr | None = None
    GroupARN: StrictStr | None = None
    EntitySelectorExpression: StrictStr | None = None
    Period: StrictInt | None = None
    ForecastStatistics: StrictBool | None = None
    NextToken: StrictStr | None = None
