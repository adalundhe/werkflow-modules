from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMDescribeAcmeDomainValidationRequest(BaseModel):
    AcmeDomainValidationArn: StrictStr
