from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_platform import DataSyncPlatform


class DataSyncAgentListEntry(BaseModel):
    AgentArn: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    Platform: DataSyncPlatform | None = None
