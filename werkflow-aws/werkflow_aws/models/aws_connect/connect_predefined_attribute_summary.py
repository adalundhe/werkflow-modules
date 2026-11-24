from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectPredefinedAttributeSummary(BaseModel):
    Name: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
