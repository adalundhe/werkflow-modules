from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectCreateContactFlowVersionRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowId: StrictStr
    Description: StrictStr | None = None
    FlowContentSha256: StrictStr | None = None
    ContactFlowVersion: StrictInt | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
