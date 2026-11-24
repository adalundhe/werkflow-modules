from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceCreateAliasRequest(BaseModel):
    DirectoryId: StrictStr
    Alias: StrictStr
