from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class DataZoneGetGlossaryResponse(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
    usageRestrictions: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
