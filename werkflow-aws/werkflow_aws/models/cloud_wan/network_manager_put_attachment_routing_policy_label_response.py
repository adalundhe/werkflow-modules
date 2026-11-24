from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class NetworkManagerPutAttachmentRoutingPolicyLabelResponse(BaseModel):
    CoreNetworkId: StrictStr | None = None
    AttachmentId: StrictStr | None = None
    RoutingPolicyLabel: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
