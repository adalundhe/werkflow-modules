from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DataZoneUpdateGlossaryResponse(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    description: StrictStr | None = None
    status: StrictStr | None = None
    usageRestrictions: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
