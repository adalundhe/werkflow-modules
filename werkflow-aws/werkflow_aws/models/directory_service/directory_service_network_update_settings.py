from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DirectoryServiceNetworkUpdateSettings(BaseModel):
    NetworkType: Literal['Dual-stack', 'IPv4', 'IPv6'] | None = None
    CustomerDnsIpsV6: list[StrictStr] | None = None
