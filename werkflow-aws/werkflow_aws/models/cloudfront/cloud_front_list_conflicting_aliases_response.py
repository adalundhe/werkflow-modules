from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_conflicting_aliases_list import CloudFrontConflictingAliasesList


class CloudFrontListConflictingAliasesResponse(BaseModel):
    ConflictingAliasesList: CloudFrontConflictingAliasesList | None = None
    ResponseMetadata: dict[str, Any] | None = None
