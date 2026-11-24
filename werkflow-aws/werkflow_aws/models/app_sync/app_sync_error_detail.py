from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncErrorDetail(BaseModel):
    message: StrictStr | None = None
