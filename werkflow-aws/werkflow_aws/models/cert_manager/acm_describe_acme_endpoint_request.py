from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMDescribeAcmeEndpointRequest(BaseModel):
    AcmeEndpointArn: StrictStr
