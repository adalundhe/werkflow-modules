from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_view_content import ConnectViewContent


class ConnectView(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    Type: StrictStr | None = None
    Description: StrictStr | None = None
    Version: StrictInt | None = None
    VersionDescription: StrictStr | None = None
    Content: ConnectViewContent | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ViewContentSha256: StrictStr | None = None
