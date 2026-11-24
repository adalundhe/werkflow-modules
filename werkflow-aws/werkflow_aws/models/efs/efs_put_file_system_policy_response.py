from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EFSPutFileSystemPolicyResponse(BaseModel):
    FileSystemId: StrictStr | None = None
    Policy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
