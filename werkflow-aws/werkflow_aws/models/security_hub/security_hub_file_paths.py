from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubFilePaths(BaseModel):
    FilePath: StrictStr | None = None
    FileName: StrictStr | None = None
    ResourceId: StrictStr | None = None
    Hash: StrictStr | None = None
