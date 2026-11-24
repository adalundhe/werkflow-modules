from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_lf_tag_pair import LakeFormationLFTagPair
from .lake_formation_resource import LakeFormationResource


class LakeFormationRemoveLFTagsFromResourceRequest(BaseModel):
    Resource: LakeFormationResource
    LFTags: list[LakeFormationLFTagPair]
    CatalogId: StrictStr | None = None
