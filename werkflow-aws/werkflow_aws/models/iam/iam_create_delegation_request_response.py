from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IAMCreateDelegationRequestResponse(BaseModel):
    ConsoleDeepLink: StrictStr | None = None
    DelegationRequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
