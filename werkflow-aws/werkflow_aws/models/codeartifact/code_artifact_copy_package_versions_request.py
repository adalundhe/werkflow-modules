from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class CodeArtifactCopyPackageVersionsRequest(BaseModel):
    domain: StrictStr
    sourceRepository: StrictStr
    destinationRepository: StrictStr
    format: Literal['npm', 'pypi', 'maven', 'nuget', 'generic', 'ruby', 'swift', 'cargo']
    package: StrictStr
    domainOwner: StrictStr | None = None
    namespace: StrictStr | None = None
    versions: list[StrictStr] | None = None
    versionRevisions: dict[StrictStr, StrictStr] | None = None
    allowOverwrite: StrictBool | None = None
    includeFromUpstream: StrictBool | None = None
