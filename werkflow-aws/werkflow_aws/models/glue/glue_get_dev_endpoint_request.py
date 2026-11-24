from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetDevEndpointRequest(BaseModel):
    EndpointName: StrictStr
