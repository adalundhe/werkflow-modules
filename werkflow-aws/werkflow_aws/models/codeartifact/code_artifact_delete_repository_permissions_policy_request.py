from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactDeleteRepositoryPermissionsPolicyRequest(BaseModel):
    domain: StrictStr
    repository: StrictStr
    domainOwner: StrictStr | None = None
    policyRevision: StrictStr | None = None
