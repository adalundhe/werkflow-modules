from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeprovisionIpamByoasnRequest(BaseModel):
    IpamId: StrictStr
    Asn: StrictStr
    DryRun: StrictBool | None = None
