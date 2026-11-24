from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDeleteVpcEndpointRequest(BaseModel):
    VpcEndpointId: StrictStr
