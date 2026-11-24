from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDeleteDBProxyEndpointRequest(BaseModel):
    DBProxyEndpointName: StrictStr
