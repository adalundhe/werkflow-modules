from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_lf_tag_pair import LakeFormationLFTagPair


class LakeFormationListLFTagsResponse(BaseModel):
    LFTags: list[LakeFormationLFTagPair] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
