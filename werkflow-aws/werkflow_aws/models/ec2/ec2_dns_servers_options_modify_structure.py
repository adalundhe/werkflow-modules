from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DnsServersOptionsModifyStructure(BaseModel):
    CustomDnsServers: list[StrictStr] | None = None
    Enabled: StrictBool | None = None
