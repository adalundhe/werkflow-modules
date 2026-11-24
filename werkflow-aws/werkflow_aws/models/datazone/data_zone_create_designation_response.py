from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneCreateDesignationResponse(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    designationType: StrictStr | None = None
    policy: StrictStr | None = None
    deletionProtection: StrictBool | None = None
    createdBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
