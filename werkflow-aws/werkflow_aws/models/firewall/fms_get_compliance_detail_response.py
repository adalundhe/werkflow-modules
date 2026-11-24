from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .fms_policy_compliance_detail import FMSPolicyComplianceDetail


class FMSGetComplianceDetailResponse(BaseModel):
    PolicyComplianceDetail: FMSPolicyComplianceDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
