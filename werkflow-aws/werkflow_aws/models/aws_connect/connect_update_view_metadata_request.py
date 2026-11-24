from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateViewMetadataRequest(BaseModel):
    InstanceId: StrictStr
    ViewId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
