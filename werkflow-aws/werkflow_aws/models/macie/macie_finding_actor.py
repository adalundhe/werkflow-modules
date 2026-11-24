from __future__ import annotations
from pydantic import BaseModel
from .macie_domain_details import MacieDomainDetails
from .macie_ip_address_details import MacieIpAddressDetails
from .macie_user_identity import MacieUserIdentity


class MacieFindingActor(BaseModel):
    domainDetails: MacieDomainDetails | None = None
    ipAddressDetails: MacieIpAddressDetails | None = None
    userIdentity: MacieUserIdentity | None = None
