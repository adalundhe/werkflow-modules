from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyNetworkAnomaly(BaseModel):
    BaselineBytes: StrictStr | None = None
    Deviation: StrictStr | None = None
    ProfileAgeDays: StrictInt | None = None
    RemoteService: StrictStr | None = None
    RemoteRegion: StrictStr | None = None
    Duration: StrictStr | None = None
    ResetRatio: StrictStr | None = None
    TargetHostCount: StrictInt | None = None
