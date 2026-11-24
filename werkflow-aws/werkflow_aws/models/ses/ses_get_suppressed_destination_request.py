from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetSuppressedDestinationRequest(BaseModel):
    EmailAddress: StrictStr
    TenantName: StrictStr | None = None
