from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMDeleteAcmeDomainValidationRequest(BaseModel):
    AcmeDomainValidationArn: StrictStr
