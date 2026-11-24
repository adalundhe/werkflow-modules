from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IpamCidrAuthorizationContext(BaseModel):
    Message: StrictStr | None = None
    Signature: StrictStr | None = None
