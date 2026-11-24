from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeArtifactUpdatePackageVersionsStatusRequest(BaseModel):
    domain: StrictStr
    repository: StrictStr
    format: Literal['npm', 'pypi', 'maven', 'nuget', 'generic', 'ruby', 'swift', 'cargo']
    package: StrictStr
    versions: list[StrictStr]
    targetStatus: Literal['Published', 'Unfinished', 'Unlisted', 'Archived', 'Disposed', 'Deleted']
    domainOwner: StrictStr | None = None
    namespace: StrictStr | None = None
    versionRevisions: dict[StrictStr, StrictStr] | None = None
    expectedStatus: Literal['Published', 'Unfinished', 'Unlisted', 'Archived', 'Disposed', 'Deleted'] | None = None
