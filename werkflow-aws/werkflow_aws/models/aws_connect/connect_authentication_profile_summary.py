from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectAuthenticationProfileSummary(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    IsDefault: StrictBool | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
