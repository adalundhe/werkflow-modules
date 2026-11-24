from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_attachment import NetworkManagerAttachment
from .network_manager_connect_attachment_options import NetworkManagerConnectAttachmentOptions


class NetworkManagerConnectAttachment(BaseModel):
    Attachment: NetworkManagerAttachment | None = None
    TransportAttachmentId: StrictStr | None = None
    Options: NetworkManagerConnectAttachmentOptions | None = None
