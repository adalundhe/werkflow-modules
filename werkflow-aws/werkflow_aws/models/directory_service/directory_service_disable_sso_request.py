from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDisableSsoRequest(BaseModel):
    DirectoryId: StrictStr
    UserName: StrictStr | None = None
    Password: StrictStr | None = None
