from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncGetChannelNamespaceRequest(BaseModel):
    apiId: StrictStr
    name: StrictStr
