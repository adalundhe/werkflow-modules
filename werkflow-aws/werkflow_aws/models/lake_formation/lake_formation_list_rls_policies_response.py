from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_rls_policy import LakeFormationRLSPolicy


class LakeFormationListRLSPoliciesResponse(BaseModel):
    RLSPolicies: list[LakeFormationRLSPolicy] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
