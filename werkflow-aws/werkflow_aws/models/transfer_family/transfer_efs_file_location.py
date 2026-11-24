from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferEfsFileLocation(BaseModel):
    FileSystemId: StrictStr | None = None
    Path: StrictStr | None = None
