from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53DomainsDnssecKey(BaseModel):
    Algorithm: StrictInt | None = None
    Flags: StrictInt | None = None
    PublicKey: StrictStr | None = None
    DigestType: StrictInt | None = None
    Digest: StrictStr | None = None
    KeyTag: StrictInt | None = None
    Id: StrictStr | None = None
