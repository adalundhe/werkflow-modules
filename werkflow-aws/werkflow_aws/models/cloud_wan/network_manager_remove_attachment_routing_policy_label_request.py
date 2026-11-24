from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerRemoveAttachmentRoutingPolicyLabelRequest(BaseModel):
    CoreNetworkId: StrictStr
    AttachmentId: StrictStr
