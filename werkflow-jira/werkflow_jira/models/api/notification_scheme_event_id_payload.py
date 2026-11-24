from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NotificationSchemeEventIDPayload(BaseModel):
    id: StrictStr | None = None
