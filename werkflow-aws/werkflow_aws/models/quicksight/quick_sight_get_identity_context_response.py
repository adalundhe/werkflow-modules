from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightGetIdentityContextResponse(BaseModel):
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    Context: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
