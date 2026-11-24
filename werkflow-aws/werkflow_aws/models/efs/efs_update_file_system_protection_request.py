from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EFSUpdateFileSystemProtectionRequest(BaseModel):
    FileSystemId: StrictStr
    ReplicationOverwriteProtection: Literal['ENABLED', 'DISABLED', 'REPLICATING'] | None = None
