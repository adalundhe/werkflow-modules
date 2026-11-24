from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_attachment import NetworkManagerAttachment


class NetworkManagerListAttachmentsResponse(BaseModel):
    Attachments: list[NetworkManagerAttachment] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
