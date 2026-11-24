from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class FSxOntapSnapshotConfiguration(BaseModel):
    SizeInMegabytes: StrictInt | None = None
    SnapmirrorLabel: StrictStr | None = None
    ExpiryTime: datetime.datetime | StrictStr | None = None
    SnaplockExpiryTime: datetime.datetime | StrictStr | None = None
    UUID: StrictStr | None = None
