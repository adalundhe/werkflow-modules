from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactDomainEntryPoint(BaseModel):
    repositoryName: StrictStr | None = None
    externalConnectionName: StrictStr | None = None
