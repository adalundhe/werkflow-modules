from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactAssociateExternalConnectionRequest(BaseModel):
    domain: StrictStr
    repository: StrictStr
    externalConnection: StrictStr
    domainOwner: StrictStr | None = None
