from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MemoryDBListAllowedNodeTypeUpdatesResponse(BaseModel):
    ScaleUpNodeTypes: list[StrictStr] | None = None
    ScaleDownNodeTypes: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
