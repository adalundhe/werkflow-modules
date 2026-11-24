from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsTransferDomainToAnotherAwsAccountRequest(BaseModel):
    DomainName: StrictStr
    AccountId: StrictStr
