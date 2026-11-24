from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ecr_encryption_configuration_for_repository_creation_template import ECREncryptionConfigurationForRepositoryCreationTemplate
from .ecr_image_tag_mutability_exclusion_filter import ECRImageTagMutabilityExclusionFilter
from .ecr_tag import ECRTag


class ECRUpdateRepositoryCreationTemplateRequest(BaseModel):
    prefix: StrictStr
    description: StrictStr | None = None
    encryptionConfiguration: ECREncryptionConfigurationForRepositoryCreationTemplate | None = None
    resourceTags: list[ECRTag] | None = None
    imageTagMutability: Literal['MUTABLE', 'IMMUTABLE', 'IMMUTABLE_WITH_EXCLUSION', 'MUTABLE_WITH_EXCLUSION'] | None = None
    imageTagMutabilityExclusionFilters: list[ECRImageTagMutabilityExclusionFilter] | None = None
    repositoryPolicy: StrictStr | None = None
    lifecyclePolicy: StrictStr | None = None
    appliedFor: list[Literal['REPLICATION', 'PULL_THROUGH_CACHE', 'CREATE_ON_PUSH']] | None = None
    customRoleArn: StrictStr | None = None
