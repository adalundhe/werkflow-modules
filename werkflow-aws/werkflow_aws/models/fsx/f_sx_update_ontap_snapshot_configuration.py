from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class FSxUpdateOntapSnapshotConfiguration(BaseModel):
    SnapmirrorLabel: StrictStr | None = None
    ExpiryTime: datetime.datetime | StrictStr | None = None
    SnaplockExpiryTime: datetime.datetime | StrictStr | None = None
