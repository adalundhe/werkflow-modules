from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ecr_encryption_configuration_for_repository_creation_template import ECREncryptionConfigurationForRepositoryCreationTemplate
from .ecr_image_tag_mutability_exclusion_filter import ECRImageTagMutabilityExclusionFilter
from .ecr_tag import ECRTag


class ECRRepositoryCreationTemplate(BaseModel):
    prefix: StrictStr | None = None
    description: StrictStr | None = None
    encryptionConfiguration: ECREncryptionConfigurationForRepositoryCreationTemplate | None = None
    resourceTags: list[ECRTag] | None = None
    imageTagMutability: StrictStr | None = None
    imageTagMutabilityExclusionFilters: list[ECRImageTagMutabilityExclusionFilter] | None = None
    repositoryPolicy: StrictStr | None = None
    lifecyclePolicy: StrictStr | None = None
    appliedFor: list[StrictStr] | None = None
    customRoleArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
