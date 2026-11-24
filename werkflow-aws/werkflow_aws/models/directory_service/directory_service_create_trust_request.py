from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DirectoryServiceCreateTrustRequest(BaseModel):
    DirectoryId: StrictStr
    RemoteDomainName: StrictStr
    TrustPassword: StrictStr
    TrustDirection: Literal['One-Way: Outgoing', 'One-Way: Incoming', 'Two-Way']
    TrustType: Literal['Forest', 'External'] | None = None
    ConditionalForwarderIpAddrs: list[StrictStr] | None = None
    ConditionalForwarderIpv6Addrs: list[StrictStr] | None = None
    SelectiveAuth: Literal['Enabled', 'Disabled'] | None = None
