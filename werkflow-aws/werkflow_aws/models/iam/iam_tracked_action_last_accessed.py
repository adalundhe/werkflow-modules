from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IAMTrackedActionLastAccessed(BaseModel):
    ActionName: StrictStr | None = None
    LastAccessedEntity: StrictStr | None = None
    LastAccessedTime: datetime.datetime | StrictStr | None = None
    LastAccessedRegion: StrictStr | None = None
