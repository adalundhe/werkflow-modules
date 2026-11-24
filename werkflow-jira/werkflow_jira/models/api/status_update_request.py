from __future__ import annotations
from pydantic import BaseModel
from .status_update import StatusUpdate


class StatusUpdateRequest(BaseModel):
    statuses: list[StatusUpdate] | None = None
