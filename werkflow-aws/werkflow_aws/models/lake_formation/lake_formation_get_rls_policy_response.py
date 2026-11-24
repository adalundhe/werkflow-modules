from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lake_formation_rls_policy import LakeFormationRLSPolicy


class LakeFormationGetRLSPolicyResponse(BaseModel):
    RLSPolicy: LakeFormationRLSPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
