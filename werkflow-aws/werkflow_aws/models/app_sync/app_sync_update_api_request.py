from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_event_config import AppSyncEventConfig


class AppSyncUpdateApiRequest(BaseModel):
    apiId: StrictStr
    name: StrictStr
    eventConfig: AppSyncEventConfig
    ownerContact: StrictStr | None = None
