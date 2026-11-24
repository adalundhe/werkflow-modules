from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_domain_unit_owner_properties import DataZoneDomainUnitOwnerProperties


class DataZoneGetDomainUnitResponse(BaseModel):
    id: StrictStr | None = None
    domainId: StrictStr | None = None
    name: StrictStr | None = None
    parentDomainUnitId: StrictStr | None = None
    description: StrictStr | None = None
    owners: list[DataZoneDomainUnitOwnerProperties] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    lastUpdatedBy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
