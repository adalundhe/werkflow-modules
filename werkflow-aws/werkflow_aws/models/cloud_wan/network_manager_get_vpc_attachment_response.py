from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_vpc_attachment import NetworkManagerVpcAttachment


class NetworkManagerGetVpcAttachmentResponse(BaseModel):
    VpcAttachment: NetworkManagerVpcAttachment | None = None
    ResponseMetadata: dict[str, Any] | None = None
