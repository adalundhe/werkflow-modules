from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceEnableSsoRequest(BaseModel):
    DirectoryId: StrictStr
    UserName: StrictStr | None = None
    Password: StrictStr | None = None
