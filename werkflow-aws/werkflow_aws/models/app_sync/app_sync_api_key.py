from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppSyncApiKey(BaseModel):
    id: StrictStr | None = None
    description: StrictStr | None = None
    expires: StrictInt | None = None
    deletes: StrictInt | None = None
