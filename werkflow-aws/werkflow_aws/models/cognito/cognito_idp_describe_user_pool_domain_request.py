from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDescribeUserPoolDomainRequest(BaseModel):
    Domain: StrictStr
