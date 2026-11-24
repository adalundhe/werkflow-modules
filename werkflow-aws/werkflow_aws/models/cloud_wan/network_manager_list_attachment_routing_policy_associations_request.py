from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerListAttachmentRoutingPolicyAssociationsRequest(BaseModel):
    CoreNetworkId: StrictStr
    AttachmentId: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
