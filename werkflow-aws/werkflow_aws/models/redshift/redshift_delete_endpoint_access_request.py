from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteEndpointAccessRequest(BaseModel):
    EndpointName: StrictStr
