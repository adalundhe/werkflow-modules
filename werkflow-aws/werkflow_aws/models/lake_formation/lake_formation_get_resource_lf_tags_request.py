from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .lake_formation_resource import LakeFormationResource


class LakeFormationGetResourceLFTagsRequest(BaseModel):
    Resource: LakeFormationResource
    CatalogId: StrictStr | None = None
    ShowAssignedLFTags: StrictBool | None = None
