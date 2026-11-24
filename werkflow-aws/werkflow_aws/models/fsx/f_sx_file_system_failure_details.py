from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxFileSystemFailureDetails(BaseModel):
    Message: StrictStr | None = None
