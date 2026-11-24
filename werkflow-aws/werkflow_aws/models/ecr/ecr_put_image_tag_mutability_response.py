from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_image_tag_mutability_exclusion_filter import ECRImageTagMutabilityExclusionFilter


class ECRPutImageTagMutabilityResponse(BaseModel):
    registryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    imageTagMutability: StrictStr | None = None
    imageTagMutabilityExclusionFilters: list[ECRImageTagMutabilityExclusionFilter] | None = None
    ResponseMetadata: dict[str, Any] | None = None
