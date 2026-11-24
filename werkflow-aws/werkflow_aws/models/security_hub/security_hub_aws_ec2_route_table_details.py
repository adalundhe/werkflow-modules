from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_association_set_details import SecurityHubAssociationSetDetails
from .security_hub_propagating_vgw_set_details import SecurityHubPropagatingVgwSetDetails
from .security_hub_route_set_details import SecurityHubRouteSetDetails


class SecurityHubAwsEc2RouteTableDetails(BaseModel):
    AssociationSet: list[SecurityHubAssociationSetDetails] | None = None
    OwnerId: StrictStr | None = None
    PropagatingVgwSet: list[SecurityHubPropagatingVgwSetDetails] | None = None
    RouteTableId: StrictStr | None = None
    RouteSet: list[SecurityHubRouteSetDetails] | None = None
    VpcId: StrictStr | None = None
