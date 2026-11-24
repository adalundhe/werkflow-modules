from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_routing_policy_association_detail import NetworkManagerRoutingPolicyAssociationDetail


class NetworkManagerCoreNetworkChangeEventValues(BaseModel):
    EdgeLocation: StrictStr | None = None
    PeerEdgeLocation: StrictStr | None = None
    RoutingPolicyDirection: StrictStr | None = None
    SegmentName: StrictStr | None = None
    NetworkFunctionGroupName: StrictStr | None = None
    AttachmentId: StrictStr | None = None
    Cidr: StrictStr | None = None
    RoutingPolicyAssociationDetails: list[NetworkManagerRoutingPolicyAssociationDetail] | None = None
