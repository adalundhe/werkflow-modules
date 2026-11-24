from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxOntapWindowsFileSystemUser(BaseModel):
    Name: StrictStr | None = None
