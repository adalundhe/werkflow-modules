from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailPortInfo(BaseModel):
    fromPort: StrictInt | None = None
    toPort: StrictInt | None = None
    protocol: Literal['tcp', 'all', 'udp', 'icmp', 'icmpv6'] | None = None
    cidrs: list[StrictStr] | None = None
    ipv6Cidrs: list[StrictStr] | None = None
    cidrListAliases: list[StrictStr] | None = None
