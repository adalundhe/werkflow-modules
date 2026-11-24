from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeAwsIdentity(BaseModel):
    externalId: StrictStr | None = None
    principal: StrictStr | None = None
