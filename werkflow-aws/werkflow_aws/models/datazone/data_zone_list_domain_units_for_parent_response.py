from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_domain_unit_summary import DataZoneDomainUnitSummary


class DataZoneListDomainUnitsForParentResponse(BaseModel):
    items: list[DataZoneDomainUnitSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
