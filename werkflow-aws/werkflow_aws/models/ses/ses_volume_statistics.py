from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SESVolumeStatistics(BaseModel):
    InboxRawCount: StrictInt | None = None
    SpamRawCount: StrictInt | None = None
    ProjectedInbox: StrictInt | None = None
    ProjectedSpam: StrictInt | None = None
