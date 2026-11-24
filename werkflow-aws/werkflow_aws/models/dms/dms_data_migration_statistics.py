from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class DMSDataMigrationStatistics(BaseModel):
    TablesLoaded: StrictInt | None = None
    ElapsedTimeMillis: StrictInt | None = None
    TablesLoading: StrictInt | None = None
    FullLoadPercentage: StrictInt | None = None
    CDCLatency: StrictInt | None = None
    TablesQueued: StrictInt | None = None
    TablesErrored: StrictInt | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    StopTime: datetime.datetime | StrictStr | None = None
