from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSTestConnectionRequest(BaseModel):
    ReplicationInstanceArn: StrictStr
    EndpointArn: StrictStr
