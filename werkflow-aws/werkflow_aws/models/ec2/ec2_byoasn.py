from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Byoasn(BaseModel):
    Asn: StrictStr | None = None
    IpamId: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    State: StrictStr | None = None
