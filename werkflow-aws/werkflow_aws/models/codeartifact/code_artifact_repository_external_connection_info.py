from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactRepositoryExternalConnectionInfo(BaseModel):
    externalConnectionName: StrictStr | None = None
    packageFormat: StrictStr | None = None
    status: StrictStr | None = None
