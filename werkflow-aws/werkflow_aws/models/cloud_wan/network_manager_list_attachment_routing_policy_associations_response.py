from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_attachment_routing_policy_association_summary import NetworkManagerAttachmentRoutingPolicyAssociationSummary


class NetworkManagerListAttachmentRoutingPolicyAssociationsResponse(BaseModel):
    AttachmentRoutingPolicyAssociations: list[NetworkManagerAttachmentRoutingPolicyAssociationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
