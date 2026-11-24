from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_sync_channel_namespace import AppSyncChannelNamespace


class AppSyncGetChannelNamespaceResponse(BaseModel):
    channelNamespace: AppSyncChannelNamespace | None = None
    ResponseMetadata: dict[str, Any] | None = None
