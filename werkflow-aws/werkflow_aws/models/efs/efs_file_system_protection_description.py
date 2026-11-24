from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EFSFileSystemProtectionDescription(BaseModel):
    ReplicationOverwriteProtection: StrictStr | None = None
