from __future__ import annotations
from pydantic import BaseModel
from .fms_account_scope import FMSAccountScope
from .fms_organizational_unit_scope import FMSOrganizationalUnitScope
from .fms_policy_type_scope import FMSPolicyTypeScope
from .fms_region_scope import FMSRegionScope


class FMSAdminScope(BaseModel):
    AccountScope: FMSAccountScope | None = None
    OrganizationalUnitScope: FMSOrganizationalUnitScope | None = None
    RegionScope: FMSRegionScope | None = None
    PolicyTypeScope: FMSPolicyTypeScope | None = None
