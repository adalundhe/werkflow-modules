from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectNotification(BaseModel):
    Content: dict[StrictStr, StrictStr] | None = None
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Priority: StrictStr | None = None
    Recipients: list[StrictStr] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    ExpiresAt: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
