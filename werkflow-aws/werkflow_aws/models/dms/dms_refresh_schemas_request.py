from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSRefreshSchemasRequest(BaseModel):
    EndpointArn: StrictStr
    ReplicationInstanceArn: StrictStr
