from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class EFSUpdateFileSystemRequest(BaseModel):
    FileSystemId: StrictStr
    ThroughputMode: Literal['bursting', 'provisioned', 'elastic'] | None = None
    ProvisionedThroughputInMibps: StrictFloat | StrictInt | None = None
