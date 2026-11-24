from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class TransferListSecurityPoliciesResponse(BaseModel):
    NextToken: StrictStr | None = None
    SecurityPolicyNames: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
