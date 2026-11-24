from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDeleteSuppressedDestinationRequest(BaseModel):
    EmailAddress: StrictStr
    TenantName: StrictStr | None = None
