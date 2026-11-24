from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53DomainsDnssecSigningAttributes(BaseModel):
    Algorithm: StrictInt | None = None
    Flags: StrictInt | None = None
    PublicKey: StrictStr | None = None
