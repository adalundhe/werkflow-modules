from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idpcimd_policy_summary_type import CognitoIDPCIMDPolicySummaryType


class CognitoIDPListCIMDPoliciesResponse(BaseModel):
    NextToken: StrictStr | None = None
    CIMDPolicies: list[CognitoIDPCIMDPolicySummaryType] | None = None
    ResponseMetadata: dict[str, Any] | None = None
