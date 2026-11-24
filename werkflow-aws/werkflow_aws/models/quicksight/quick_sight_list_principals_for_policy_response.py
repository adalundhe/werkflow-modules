from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_policy_principal import QuickSightPolicyPrincipal


class QuickSightListPrincipalsForPolicyResponse(BaseModel):
    Principals: list[QuickSightPolicyPrincipal] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
