from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class FSxDeleteFileCacheResponse(BaseModel):
    FileCacheId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
