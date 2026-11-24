from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeArtifactGetPackageVersionAssetRequest(BaseModel):
    domain: StrictStr
    repository: StrictStr
    format: Literal['npm', 'pypi', 'maven', 'nuget', 'generic', 'ruby', 'swift', 'cargo']
    package: StrictStr
    packageVersion: StrictStr
    asset: StrictStr
    domainOwner: StrictStr | None = None
    namespace: StrictStr | None = None
    packageVersionRevision: StrictStr | None = None
