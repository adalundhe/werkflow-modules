from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AssociateIpamByoasnRequest(BaseModel):
    Asn: StrictStr
    Cidr: StrictStr
    DryRun: StrictBool | None = None
