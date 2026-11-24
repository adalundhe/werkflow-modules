from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMDescribeAcmeAccountRequest(BaseModel):
    AcmeEndpointArn: StrictStr
    AccountUrl: StrictStr
