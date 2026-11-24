from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_integration import AppSyncIntegration


class AppSyncHandlerConfig(BaseModel):
    behavior: StrictStr | None = None
    integration: AppSyncIntegration | None = None
