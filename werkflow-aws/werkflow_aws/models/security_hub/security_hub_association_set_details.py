from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_association_state_details import SecurityHubAssociationStateDetails


class SecurityHubAssociationSetDetails(BaseModel):
    AssociationState: SecurityHubAssociationStateDetails | None = None
    GatewayId: StrictStr | None = None
    Main: StrictBool | None = None
    RouteTableAssociationId: StrictStr | None = None
    RouteTableId: StrictStr | None = None
    SubnetId: StrictStr | None = None
