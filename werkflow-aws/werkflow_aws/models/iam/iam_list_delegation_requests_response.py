from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_delegation_request import IAMDelegationRequest


class IAMListDelegationRequestsResponse(BaseModel):
    DelegationRequests: list[IAMDelegationRequest] | None = None
    Marker: StrictStr | None = None
    isTruncated: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
