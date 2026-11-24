from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectNotificationSearchSummary(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    InstanceId: StrictStr | None = None
    Content: dict[StrictStr, StrictStr] | None = None
    Priority: StrictStr | None = None
    Recipients: list[StrictStr] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    ExpiresAt: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
