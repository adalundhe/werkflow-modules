from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectContactFlowAliasSummary(BaseModel):
    Arn: StrictStr | None = None
    AliasId: StrictStr | None = None
    Version: StrictInt | None = None
    AliasName: StrictStr | None = None
    AliasDescription: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
