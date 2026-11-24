from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactDescribeRepositoryRequest(BaseModel):
    domain: StrictStr
    repository: StrictStr
    domainOwner: StrictStr | None = None
