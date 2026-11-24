from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_sync_channel_namespace import AppSyncChannelNamespace


class AppSyncListChannelNamespacesResponse(BaseModel):
    channelNamespaces: list[AppSyncChannelNamespace] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
