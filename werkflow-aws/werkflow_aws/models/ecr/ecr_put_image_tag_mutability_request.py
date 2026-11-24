from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ecr_image_tag_mutability_exclusion_filter import ECRImageTagMutabilityExclusionFilter


class ECRPutImageTagMutabilityRequest(BaseModel):
    repositoryName: StrictStr
    imageTagMutability: Literal['MUTABLE', 'IMMUTABLE', 'IMMUTABLE_WITH_EXCLUSION', 'MUTABLE_WITH_EXCLUSION']
    registryId: StrictStr | None = None
    imageTagMutabilityExclusionFilters: list[ECRImageTagMutabilityExclusionFilter] | None = None
