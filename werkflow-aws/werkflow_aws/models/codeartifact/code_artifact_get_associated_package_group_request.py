from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeArtifactGetAssociatedPackageGroupRequest(BaseModel):
    domain: StrictStr
    format: Literal['npm', 'pypi', 'maven', 'nuget', 'generic', 'ruby', 'swift', 'cargo']
    package: StrictStr
    domainOwner: StrictStr | None = None
    namespace: StrictStr | None = None
