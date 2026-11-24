from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceEnableDirectoryDataAccessRequest(BaseModel):
    DirectoryId: StrictStr
