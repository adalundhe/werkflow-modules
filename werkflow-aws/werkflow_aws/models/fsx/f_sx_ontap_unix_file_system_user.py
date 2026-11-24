from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxOntapUnixFileSystemUser(BaseModel):
    Name: StrictStr | None = None
