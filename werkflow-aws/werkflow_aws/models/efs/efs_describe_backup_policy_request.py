from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EFSDescribeBackupPolicyRequest(BaseModel):
    FileSystemId: StrictStr
