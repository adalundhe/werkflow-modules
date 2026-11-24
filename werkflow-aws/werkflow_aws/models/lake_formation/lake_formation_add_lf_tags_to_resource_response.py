from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lake_formation_lf_tag_error import LakeFormationLFTagError


class LakeFormationAddLFTagsToResourceResponse(BaseModel):
    Failures: list[LakeFormationLFTagError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
