from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieIpOwner(BaseModel):
    asn: StrictStr | None = None
    asnOrg: StrictStr | None = None
    isp: StrictStr | None = None
    org: StrictStr | None = None
