from __future__ import annotations
from pydantic import BaseModel
from .lake_formation_error_detail import LakeFormationErrorDetail
from .lake_formation_lf_tag_pair import LakeFormationLFTagPair


class LakeFormationLFTagError(BaseModel):
    LFTag: LakeFormationLFTagPair | None = None
    Error: LakeFormationErrorDetail | None = None
