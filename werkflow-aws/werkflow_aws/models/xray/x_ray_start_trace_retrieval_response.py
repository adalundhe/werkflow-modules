from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class XRayStartTraceRetrievalResponse(BaseModel):
    RetrievalToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
