from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceRejectSharedDirectoryRequest(BaseModel):
    SharedDirectoryId: StrictStr
