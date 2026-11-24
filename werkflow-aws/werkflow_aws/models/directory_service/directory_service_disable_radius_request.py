from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDisableRadiusRequest(BaseModel):
    DirectoryId: StrictStr
