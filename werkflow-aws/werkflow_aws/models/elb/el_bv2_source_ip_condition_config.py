from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2SourceIpConditionConfig(BaseModel):
    Values: list[StrictStr] | None = None
    IpAddressType: StrictStr | None = None
