from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2DeviceOptions(BaseModel):
    TenantId: StrictStr | None = None
    PublicSigningKeyUrl: StrictStr | None = None
