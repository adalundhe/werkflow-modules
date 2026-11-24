from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lake_formation_column_lf_tag import LakeFormationColumnLFTag
from .lake_formation_lf_tag_pair import LakeFormationLFTagPair


class LakeFormationGetResourceLFTagsResponse(BaseModel):
    LFTagOnDatabase: list[LakeFormationLFTagPair] | None = None
    LFTagsOnTable: list[LakeFormationLFTagPair] | None = None
    LFTagsOnColumns: list[LakeFormationColumnLFTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
