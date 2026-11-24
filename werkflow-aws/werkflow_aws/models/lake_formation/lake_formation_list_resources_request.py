from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lake_formation_filter_condition import LakeFormationFilterCondition


class LakeFormationListResourcesRequest(BaseModel):
    FilterConditionList: list[LakeFormationFilterCondition] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
