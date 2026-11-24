from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDeleteConnectionRequest(BaseModel):
    EndpointArn: StrictStr
    ReplicationInstanceArn: StrictStr
