from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .iam_delegation_request import IAMDelegationRequest


class IAMGetDelegationRequestResponse(BaseModel):
    DelegationRequest: IAMDelegationRequest | None = None
    PermissionCheckStatus: StrictStr | None = None
    PermissionCheckResult: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
