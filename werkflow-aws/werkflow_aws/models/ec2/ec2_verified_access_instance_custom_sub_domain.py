from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2VerifiedAccessInstanceCustomSubDomain(BaseModel):
    SubDomain: StrictStr | None = None
    Nameservers: list[StrictStr] | None = None
