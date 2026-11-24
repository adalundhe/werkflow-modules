from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ManagedBlockchainCreateAccessorResponse(BaseModel):
    AccessorId: StrictStr | None = None
    BillingToken: StrictStr | None = None
    NetworkType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
