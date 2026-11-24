from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lake_formation_resource_info import LakeFormationResourceInfo


class LakeFormationDescribeResourceResponse(BaseModel):
    ResourceInfo: LakeFormationResourceInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
