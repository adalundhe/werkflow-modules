from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_connect_attachment import NetworkManagerConnectAttachment


class NetworkManagerCreateConnectAttachmentResponse(BaseModel):
    ConnectAttachment: NetworkManagerConnectAttachment | None = None
    ResponseMetadata: dict[str, Any] | None = None
