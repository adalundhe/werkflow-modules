from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .code_artifact_package_origin_restrictions import CodeArtifactPackageOriginRestrictions


class CodeArtifactPutPackageOriginConfigurationRequest(BaseModel):
    domain: StrictStr
    repository: StrictStr
    format: Literal['npm', 'pypi', 'maven', 'nuget', 'generic', 'ruby', 'swift', 'cargo']
    package: StrictStr
    restrictions: CodeArtifactPackageOriginRestrictions
    domainOwner: StrictStr | None = None
    namespace: StrictStr | None = None
