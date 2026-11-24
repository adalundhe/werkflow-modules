from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectContactFlow(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    State: StrictStr | None = None
    Status: StrictStr | None = None
    Description: StrictStr | None = None
    Content: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    FlowContentSha256: StrictStr | None = None
    Version: StrictInt | None = None
    VersionDescription: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
