from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneDesignationSummary(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    designationType: StrictStr | None = None
    deletionProtection: StrictBool | None = None
    createdBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
