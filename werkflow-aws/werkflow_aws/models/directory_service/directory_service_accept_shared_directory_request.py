from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceAcceptSharedDirectoryRequest(BaseModel):
    SharedDirectoryId: StrictStr
