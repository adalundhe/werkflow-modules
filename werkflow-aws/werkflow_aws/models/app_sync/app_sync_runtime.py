from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncRuntime(BaseModel):
    name: StrictStr | None = None
    runtimeVersion: StrictStr | None = None
