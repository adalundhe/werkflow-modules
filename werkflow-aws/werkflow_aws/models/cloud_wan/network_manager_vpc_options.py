from __future__ import annotations
from pydantic import BaseModel, StrictBool


class NetworkManagerVpcOptions(BaseModel):
    Ipv6Support: StrictBool | None = None
    ApplianceModeSupport: StrictBool | None = None
    DnsSupport: StrictBool | None = None
    SecurityGroupReferencingSupport: StrictBool | None = None
