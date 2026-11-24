from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idpcimd_policy_type import CognitoIDPCIMDPolicyType


class CognitoIDPCreateCIMDPolicyResponse(BaseModel):
    CIMDPolicy: CognitoIDPCIMDPolicyType | None = None
    ResponseMetadata: dict[str, Any] | None = None
