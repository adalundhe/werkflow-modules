from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactDeleteDomainPermissionsPolicyRequest(BaseModel):
    domain: StrictStr
    domainOwner: StrictStr | None = None
    policyRevision: StrictStr | None = None
