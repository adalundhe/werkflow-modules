from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .code_artifact_package_group_allowed_repository import CodeArtifactPackageGroupAllowedRepository


class CodeArtifactUpdatePackageGroupOriginConfigurationRequest(BaseModel):
    domain: StrictStr
    packageGroup: StrictStr
    domainOwner: StrictStr | None = None
    restrictions: dict[Literal['EXTERNAL_UPSTREAM', 'INTERNAL_UPSTREAM', 'PUBLISH'], Literal['ALLOW', 'ALLOW_SPECIFIC_REPOSITORIES', 'BLOCK', 'INHERIT']] | None = None
    addAllowedRepositories: list[CodeArtifactPackageGroupAllowedRepository] | None = None
    removeAllowedRepositories: list[CodeArtifactPackageGroupAllowedRepository] | None = None
