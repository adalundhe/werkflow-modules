from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxReleaseFileSystemNfsV3LocksRequest(BaseModel):
    FileSystemId: StrictStr
    ClientRequestToken: StrictStr | None = None
