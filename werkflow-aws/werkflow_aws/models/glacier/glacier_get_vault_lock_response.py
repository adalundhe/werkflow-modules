from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlacierGetVaultLockResponse(BaseModel):
    Policy: StrictStr | None = None
    State: StrictStr | None = None
    ExpirationDate: StrictStr | None = None
    CreationDate: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
