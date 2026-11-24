from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DirectoryServiceUpdateTrustResponse(BaseModel):
    RequestId: StrictStr | None = None
    TrustId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
