from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeArtifactDescribePackageVersionRequest(BaseModel):
    domain: StrictStr
    repository: StrictStr
    format: Literal['npm', 'pypi', 'maven', 'nuget', 'generic', 'ruby', 'swift', 'cargo']
    package: StrictStr
    packageVersion: StrictStr
    domainOwner: StrictStr | None = None
    namespace: StrictStr | None = None
