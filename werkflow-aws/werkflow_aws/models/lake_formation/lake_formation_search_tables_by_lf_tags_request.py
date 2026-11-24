from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lake_formation_lf_tag import LakeFormationLFTag


class LakeFormationSearchTablesByLFTagsRequest(BaseModel):
    Expression: list[LakeFormationLFTag]
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    CatalogId: StrictStr | None = None
