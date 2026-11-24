from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DMSDescribeSchemasResponse(BaseModel):
    Marker: StrictStr | None = None
    Schemas: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
