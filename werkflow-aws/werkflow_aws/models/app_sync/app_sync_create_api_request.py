from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_event_config import AppSyncEventConfig


class AppSyncCreateApiRequest(BaseModel):
    name: StrictStr
    eventConfig: AppSyncEventConfig
    ownerContact: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
