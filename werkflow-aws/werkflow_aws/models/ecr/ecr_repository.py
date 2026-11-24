from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ecr_encryption_configuration import ECREncryptionConfiguration
from .ecr_image_scanning_configuration import ECRImageScanningConfiguration
from .ecr_image_tag_mutability_exclusion_filter import ECRImageTagMutabilityExclusionFilter


class ECRRepository(BaseModel):
    repositoryArn: StrictStr | None = None
    registryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    repositoryUri: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    imageTagMutability: StrictStr | None = None
    imageTagMutabilityExclusionFilters: list[ECRImageTagMutabilityExclusionFilter] | None = None
    imageScanningConfiguration: ECRImageScanningConfiguration | None = None
    encryptionConfiguration: ECREncryptionConfiguration | None = None
