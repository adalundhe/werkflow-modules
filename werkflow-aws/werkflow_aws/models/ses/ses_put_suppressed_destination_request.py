from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SESPutSuppressedDestinationRequest(BaseModel):
    EmailAddress: StrictStr
    Reason: Literal['BOUNCE', 'COMPLAINT']
    TenantName: StrictStr | None = None
