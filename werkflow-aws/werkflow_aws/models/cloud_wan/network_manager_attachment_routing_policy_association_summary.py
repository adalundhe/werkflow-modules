from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerAttachmentRoutingPolicyAssociationSummary(BaseModel):
    AttachmentId: StrictStr | None = None
    PendingRoutingPolicies: list[StrictStr] | None = None
    AssociatedRoutingPolicies: list[StrictStr] | None = None
    RoutingPolicyLabel: StrictStr | None = None
