from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_policy_grant_detail import DataZonePolicyGrantDetail
from .data_zone_policy_grant_principal import DataZonePolicyGrantPrincipal


class DataZonePolicyGrantMember(BaseModel):
    principal: DataZonePolicyGrantPrincipal | None = None
    detail: DataZonePolicyGrantDetail | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    grantId: StrictStr | None = None
