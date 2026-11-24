from __future__ import annotations
from pydantic import BaseModel
from .data_zone_domain_unit_filter_for_project import DataZoneDomainUnitFilterForProject


class DataZoneProjectGrantFilter(BaseModel):
    domainUnitFilter: DataZoneDomainUnitFilterForProject | None = None
