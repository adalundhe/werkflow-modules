from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_policy_compliance_status import FMSPolicyComplianceStatus


class FMSListComplianceStatusResponse(BaseModel):
    PolicyComplianceStatusList: list[FMSPolicyComplianceStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
