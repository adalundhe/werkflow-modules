from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_domain_unit_grant_filter import DataZoneDomainUnitGrantFilter


class DataZoneDomainUnitPolicyGrantPrincipal(BaseModel):
    domainUnitDesignation: StrictStr | None = None
    domainUnitIdentifier: StrictStr | None = None
    domainUnitGrantFilter: DataZoneDomainUnitGrantFilter | None = None
