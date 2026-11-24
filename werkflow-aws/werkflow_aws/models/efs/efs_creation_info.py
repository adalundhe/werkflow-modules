from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EFSCreationInfo(BaseModel):
    OwnerUid: StrictInt | None = None
    OwnerGid: StrictInt | None = None
    Permissions: StrictStr | None = None
