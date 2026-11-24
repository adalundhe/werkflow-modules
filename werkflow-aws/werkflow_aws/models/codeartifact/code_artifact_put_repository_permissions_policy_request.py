from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactPutRepositoryPermissionsPolicyRequest(BaseModel):
    domain: StrictStr
    repository: StrictStr
    policyDocument: StrictStr
    domainOwner: StrictStr | None = None
    policyRevision: StrictStr | None = None
