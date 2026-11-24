from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectSecurityProfileSummary(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    Type: StrictStr | None = None
