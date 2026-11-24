from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncAuthMode(BaseModel):
    authType: StrictStr | None = None
