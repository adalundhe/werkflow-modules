from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class KMSCreateGrantResponse(BaseModel):
    GrantToken: StrictStr | None = None
    GrantId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
