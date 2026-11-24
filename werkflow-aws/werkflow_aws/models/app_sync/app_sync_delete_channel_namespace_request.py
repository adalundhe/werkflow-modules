from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncDeleteChannelNamespaceRequest(BaseModel):
    apiId: StrictStr
    name: StrictStr
