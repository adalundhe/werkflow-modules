from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EFSDeleteFileSystemPolicyRequest(BaseModel):
    FileSystemId: StrictStr
