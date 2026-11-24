from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_policy_option import FMSPolicyOption


class FMSSecurityServicePolicyData(BaseModel):
    Type: StrictStr | None = None
    ManagedServiceData: StrictStr | None = None
    PolicyOption: FMSPolicyOption | None = None
