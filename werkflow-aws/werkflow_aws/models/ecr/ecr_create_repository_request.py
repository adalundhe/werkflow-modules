from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ecr_encryption_configuration import ECREncryptionConfiguration
from .ecr_image_scanning_configuration import ECRImageScanningConfiguration
from .ecr_image_tag_mutability_exclusion_filter import ECRImageTagMutabilityExclusionFilter
from .ecr_tag import ECRTag


class ECRCreateRepositoryRequest(BaseModel):
    repositoryName: StrictStr
    registryId: StrictStr | None = None
    tags: list[ECRTag] | None = None
    imageTagMutability: Literal['MUTABLE', 'IMMUTABLE', 'IMMUTABLE_WITH_EXCLUSION', 'MUTABLE_WITH_EXCLUSION'] | None = None
    imageTagMutabilityExclusionFilters: list[ECRImageTagMutabilityExclusionFilter] | None = None
    imageScanningConfiguration: ECRImageScanningConfiguration | None = None
    encryptionConfiguration: ECREncryptionConfiguration | None = None
