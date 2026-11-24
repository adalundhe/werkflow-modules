from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_single_sign_on import DataZoneSingleSignOn


class DataZoneUpdateDomainResponse(BaseModel):
    id: StrictStr | None = None
    rootDomainUnitId: StrictStr | None = None
    description: StrictStr | None = None
    singleSignOn: DataZoneSingleSignOn | None = None
    domainExecutionRole: StrictStr | None = None
    serviceRole: StrictStr | None = None
    name: StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
