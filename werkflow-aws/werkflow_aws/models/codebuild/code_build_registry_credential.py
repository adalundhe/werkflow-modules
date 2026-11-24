from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildRegistryCredential(BaseModel):
    credential: StrictStr | None = None
    credentialProvider: StrictStr | None = None
