from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMDomainValidationOption(BaseModel):
    DomainName: StrictStr
    ValidationDomain: StrictStr
