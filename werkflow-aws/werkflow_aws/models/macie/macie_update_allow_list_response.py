from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MacieUpdateAllowListResponse(BaseModel):
    arn: StrictStr | None = None
    id: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
