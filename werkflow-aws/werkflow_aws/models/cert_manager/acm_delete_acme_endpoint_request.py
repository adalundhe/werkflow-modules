from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMDeleteAcmeEndpointRequest(BaseModel):
    AcmeEndpointArn: StrictStr
