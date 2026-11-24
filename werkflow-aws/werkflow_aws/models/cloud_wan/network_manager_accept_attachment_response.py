from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_attachment import NetworkManagerAttachment


class NetworkManagerAcceptAttachmentResponse(BaseModel):
    Attachment: NetworkManagerAttachment | None = None
    ResponseMetadata: dict[str, Any] | None = None
