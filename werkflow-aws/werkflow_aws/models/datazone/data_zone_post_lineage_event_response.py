from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DataZonePostLineageEventResponse(BaseModel):
    id: StrictStr | None = None
    domainId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
