from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_domain_summary import DataZoneDomainSummary


class DataZoneListDomainsResponse(BaseModel):
    items: list[DataZoneDomainSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
