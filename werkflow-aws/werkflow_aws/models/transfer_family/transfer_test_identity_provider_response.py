from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class TransferTestIdentityProviderResponse(BaseModel):
    Response: StrictStr | None = None
    StatusCode: StrictInt | None = None
    Message: StrictStr | None = None
    Url: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
