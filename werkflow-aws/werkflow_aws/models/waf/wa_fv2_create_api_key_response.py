from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class WAFv2CreateAPIKeyResponse(BaseModel):
    APIKey: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
