from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactDescribeDomainRequest(BaseModel):
    domain: StrictStr
    domainOwner: StrictStr | None = None
