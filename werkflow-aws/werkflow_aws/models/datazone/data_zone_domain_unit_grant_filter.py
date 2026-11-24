from __future__ import annotations
from pydantic import BaseModel
from .data_zone_all_domain_units_grant_filter import DataZoneAllDomainUnitsGrantFilter


class DataZoneDomainUnitGrantFilter(BaseModel):
    allDomainUnitsGrantFilter: DataZoneAllDomainUnitsGrantFilter | None = None
