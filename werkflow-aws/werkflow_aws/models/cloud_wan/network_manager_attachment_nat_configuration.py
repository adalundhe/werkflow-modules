from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .network_manager_nat_rule import NetworkManagerNatRule


class NetworkManagerAttachmentNatConfiguration(BaseModel):
    AttachmentId: StrictStr | None = None
    NatGatewaySupport: StrictStr | None = None
    NatSystemRouteSupport: StrictBool | None = None
    NatGatewayRules: list[NetworkManagerNatRule] | None = None
