from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxActiveDirectoryBackupAttributes(BaseModel):
    DomainName: StrictStr | None = None
    ActiveDirectoryId: StrictStr | None = None
    ResourceARN: StrictStr | None = None
