from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMRevokeAcmeAccountRequest(BaseModel):
    AcmeEndpointArn: StrictStr
    AccountUrl: StrictStr
