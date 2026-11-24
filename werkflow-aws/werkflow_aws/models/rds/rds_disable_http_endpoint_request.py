from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDisableHttpEndpointRequest(BaseModel):
    ResourceArn: StrictStr
