from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class WAFv2GetDecryptedAPIKeyResponse(BaseModel):
    TokenDomains: list[StrictStr] | None = None
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
