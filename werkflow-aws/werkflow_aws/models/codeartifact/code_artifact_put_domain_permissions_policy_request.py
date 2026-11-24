from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactPutDomainPermissionsPolicyRequest(BaseModel):
    domain: StrictStr
    policyDocument: StrictStr
    domainOwner: StrictStr | None = None
    policyRevision: StrictStr | None = None
