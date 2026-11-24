from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerPutAttachmentRoutingPolicyLabelRequest(BaseModel):
    CoreNetworkId: StrictStr
    AttachmentId: StrictStr
    RoutingPolicyLabel: StrictStr
    ClientToken: StrictStr | None = None
