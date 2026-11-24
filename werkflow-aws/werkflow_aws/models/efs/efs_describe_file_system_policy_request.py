from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EFSDescribeFileSystemPolicyRequest(BaseModel):
    FileSystemId: StrictStr
