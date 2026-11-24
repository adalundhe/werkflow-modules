from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CloudTrailImportStatistics(BaseModel):
    PrefixesFound: StrictInt | None = None
    PrefixesCompleted: StrictInt | None = None
    FilesCompleted: StrictInt | None = None
    EventsCompleted: StrictInt | None = None
    FailedEntries: StrictInt | None = None
