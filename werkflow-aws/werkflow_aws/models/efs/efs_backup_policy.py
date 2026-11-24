from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EFSBackupPolicy(BaseModel):
    Status: StrictStr | None = None
