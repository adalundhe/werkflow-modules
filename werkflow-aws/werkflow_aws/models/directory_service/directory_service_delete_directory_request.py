from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDeleteDirectoryRequest(BaseModel):
    DirectoryId: StrictStr
