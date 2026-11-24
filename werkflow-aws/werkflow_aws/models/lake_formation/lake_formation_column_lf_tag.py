from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_lf_tag_pair import LakeFormationLFTagPair


class LakeFormationColumnLFTag(BaseModel):
    Name: StrictStr | None = None
    LFTags: list[LakeFormationLFTagPair] | None = None
