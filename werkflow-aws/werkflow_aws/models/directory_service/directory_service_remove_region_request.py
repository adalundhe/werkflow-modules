from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceRemoveRegionRequest(BaseModel):
    DirectoryId: StrictStr
