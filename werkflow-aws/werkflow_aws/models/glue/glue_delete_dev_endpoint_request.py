from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteDevEndpointRequest(BaseModel):
    EndpointName: StrictStr
