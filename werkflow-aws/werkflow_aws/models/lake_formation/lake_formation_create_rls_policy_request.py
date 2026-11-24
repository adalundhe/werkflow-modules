from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_column import LakeFormationColumn


class LakeFormationCreateRLSPolicyRequest(BaseModel):
    Name: StrictStr
    AttachmentColumns: list[LakeFormationColumn]
    FilterExpression: StrictStr
