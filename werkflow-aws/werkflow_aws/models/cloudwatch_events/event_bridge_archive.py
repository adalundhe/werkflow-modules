from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeArchive(BaseModel):
    ArchiveName: StrictStr | None = None
    EventSourceArn: StrictStr | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
    RetentionDays: StrictInt | None = None
    SizeBytes: StrictInt | None = None
    EventCount: StrictInt | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
