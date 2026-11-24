from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_rls_policy_attachment import LakeFormationRLSPolicyAttachment


class LakeFormationListRLSPolicyAttachmentsResponse(BaseModel):
    RLSPolicyAttachments: list[LakeFormationRLSPolicyAttachment] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
