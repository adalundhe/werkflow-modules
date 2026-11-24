from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsAcceptDomainTransferFromAnotherAwsAccountRequest(BaseModel):
    DomainName: StrictStr
    Password: StrictStr
