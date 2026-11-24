from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceOSUpdateSettings(BaseModel):
    OSVersion: StrictStr | None = None
