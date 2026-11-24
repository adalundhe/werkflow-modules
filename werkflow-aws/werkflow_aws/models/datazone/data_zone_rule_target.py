from __future__ import annotations
from pydantic import BaseModel
from .data_zone_domain_unit_target import DataZoneDomainUnitTarget


class DataZoneRuleTarget(BaseModel):
    domainUnitTarget: DataZoneDomainUnitTarget | None = None
