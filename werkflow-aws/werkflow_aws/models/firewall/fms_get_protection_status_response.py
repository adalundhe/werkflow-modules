from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class FMSGetProtectionStatusResponse(BaseModel):
    AdminAccountId: StrictStr | None = None
    ServiceType: StrictStr | None = None
    Data: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
