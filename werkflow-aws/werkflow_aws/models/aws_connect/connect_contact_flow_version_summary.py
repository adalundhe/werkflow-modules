from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectContactFlowVersionSummary(BaseModel):
    Arn: StrictStr | None = None
    VersionDescription: StrictStr | None = None
    Version: StrictInt | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
