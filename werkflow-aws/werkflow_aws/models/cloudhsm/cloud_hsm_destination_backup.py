from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudHSMDestinationBackup(BaseModel):
    CreateTimestamp: datetime.datetime | StrictStr | None = None
    SourceRegion: StrictStr | None = None
    SourceBackup: StrictStr | None = None
    SourceCluster: StrictStr | None = None
