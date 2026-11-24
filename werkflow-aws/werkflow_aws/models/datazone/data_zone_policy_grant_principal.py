from __future__ import annotations
from pydantic import BaseModel
from .data_zone_domain_unit_policy_grant_principal import DataZoneDomainUnitPolicyGrantPrincipal
from .data_zone_group_policy_grant_principal import DataZoneGroupPolicyGrantPrincipal
from .data_zone_project_policy_grant_principal import DataZoneProjectPolicyGrantPrincipal
from .data_zone_user_policy_grant_principal import DataZoneUserPolicyGrantPrincipal


class DataZonePolicyGrantPrincipal(BaseModel):
    user: DataZoneUserPolicyGrantPrincipal | None = None
    group: DataZoneGroupPolicyGrantPrincipal | None = None
    project: DataZoneProjectPolicyGrantPrincipal | None = None
    domainUnit: DataZoneDomainUnitPolicyGrantPrincipal | None = None
