from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactDeleteRepositoryRequest(BaseModel):
    domain: StrictStr
    repository: StrictStr
    domainOwner: StrictStr | None = None
