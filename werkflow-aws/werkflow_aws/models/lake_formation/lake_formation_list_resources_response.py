from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_resource_info import LakeFormationResourceInfo


class LakeFormationListResourcesResponse(BaseModel):
    ResourceInfoList: list[LakeFormationResourceInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
