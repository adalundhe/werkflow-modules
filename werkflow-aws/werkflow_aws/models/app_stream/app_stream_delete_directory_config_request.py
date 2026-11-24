from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDeleteDirectoryConfigRequest(BaseModel):
    DirectoryName: StrictStr
