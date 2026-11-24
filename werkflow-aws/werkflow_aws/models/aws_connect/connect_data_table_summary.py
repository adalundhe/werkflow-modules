from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectDataTableSummary(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
