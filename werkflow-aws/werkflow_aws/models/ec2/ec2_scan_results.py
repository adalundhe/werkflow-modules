from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2ScanResults(BaseModel):
    HighestFindingSeverityLabel: StrictStr | None = None
    FindingScanDate: datetime.datetime | StrictStr | None = None
    InformationalFixAvailableSince: datetime.datetime | StrictStr | None = None
    LowFixAvailableSince: datetime.datetime | StrictStr | None = None
    MediumFixAvailableSince: datetime.datetime | StrictStr | None = None
    HighFixAvailableSince: datetime.datetime | StrictStr | None = None
    CriticalFixAvailableSince: datetime.datetime | StrictStr | None = None
