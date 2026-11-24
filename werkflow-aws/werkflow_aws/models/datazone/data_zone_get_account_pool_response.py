from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_account_source import DataZoneAccountSource


class DataZoneGetAccountPoolResponse(BaseModel):
    domainId: StrictStr | None = None
    name: StrictStr | None = None
    id: StrictStr | None = None
    description: StrictStr | None = None
    resolutionStrategy: StrictStr | None = None
    accountSource: DataZoneAccountSource | None = None
    createdBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
    domainUnitId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
