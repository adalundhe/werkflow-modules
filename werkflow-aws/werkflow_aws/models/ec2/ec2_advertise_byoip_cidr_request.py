from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AdvertiseByoipCidrRequest(BaseModel):
    Cidr: StrictStr
    Asn: StrictStr | None = None
    DryRun: StrictBool | None = None
    NetworkBorderGroup: StrictStr | None = None
