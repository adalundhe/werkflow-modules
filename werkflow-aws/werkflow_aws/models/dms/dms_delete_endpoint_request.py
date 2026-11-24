from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDeleteEndpointRequest(BaseModel):
    EndpointArn: StrictStr
