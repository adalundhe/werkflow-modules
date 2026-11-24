from __future__ import annotations
from pydantic import BaseModel
from .data_zone_domain_unit_group_properties import DataZoneDomainUnitGroupProperties
from .data_zone_domain_unit_user_properties import DataZoneDomainUnitUserProperties


class DataZoneDomainUnitOwnerProperties(BaseModel):
    user: DataZoneDomainUnitUserProperties | None = None
    group: DataZoneDomainUnitGroupProperties | None = None
