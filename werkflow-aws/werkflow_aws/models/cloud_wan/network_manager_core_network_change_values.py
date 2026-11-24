from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .network_manager_multipath_resilience_change_values import NetworkManagerMultipathResilienceChangeValues
from .network_manager_routing_policy_association_detail import NetworkManagerRoutingPolicyAssociationDetail
from .network_manager_service_insertion_action import NetworkManagerServiceInsertionAction


class NetworkManagerCoreNetworkChangeValues(BaseModel):
    SegmentName: StrictStr | None = None
    NetworkFunctionGroupName: StrictStr | None = None
    EdgeLocations: list[StrictStr] | None = None
    Asn: StrictInt | None = None
    Cidr: StrictStr | None = None
    DestinationIdentifier: StrictStr | None = None
    InsideCidrBlocks: list[StrictStr] | None = None
    SharedSegments: list[StrictStr] | None = None
    ServiceInsertionActions: list[NetworkManagerServiceInsertionAction] | None = None
    VpnEcmpSupport: StrictBool | None = None
    DnsSupport: StrictBool | None = None
    SecurityGroupReferencingSupport: StrictBool | None = None
    RoutingPolicyDirection: StrictStr | None = None
    RoutingPolicy: StrictStr | None = None
    PeerEdgeLocations: list[StrictStr] | None = None
    AttachmentId: StrictStr | None = None
    RoutingPolicyAssociationDetails: list[NetworkManagerRoutingPolicyAssociationDetail] | None = None
    MultipathResilience: NetworkManagerMultipathResilienceChangeValues | None = None
