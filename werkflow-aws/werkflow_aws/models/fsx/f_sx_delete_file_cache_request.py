from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxDeleteFileCacheRequest(BaseModel):
    FileCacheId: StrictStr
    ClientRequestToken: StrictStr | None = None
