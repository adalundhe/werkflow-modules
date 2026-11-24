from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncEventBridgeDataSourceConfig(BaseModel):
    eventBusArn: StrictStr | None = None
