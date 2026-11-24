from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class DMSReplicationTaskStats(BaseModel):
    FullLoadProgressPercent: StrictInt | None = None
    ElapsedTimeMillis: StrictInt | None = None
    TablesLoaded: StrictInt | None = None
    TablesLoading: StrictInt | None = None
    TablesQueued: StrictInt | None = None
    TablesErrored: StrictInt | None = None
    FreshStartDate: datetime.datetime | StrictStr | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    StopDate: datetime.datetime | StrictStr | None = None
    FullLoadStartDate: datetime.datetime | StrictStr | None = None
    FullLoadFinishDate: datetime.datetime | StrictStr | None = None
