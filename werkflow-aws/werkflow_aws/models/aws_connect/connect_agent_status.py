from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectAgentStatus(BaseModel):
    AgentStatusARN: StrictStr | None = None
    AgentStatusId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Type: StrictStr | None = None
    DisplayOrder: StrictInt | None = None
    State: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
