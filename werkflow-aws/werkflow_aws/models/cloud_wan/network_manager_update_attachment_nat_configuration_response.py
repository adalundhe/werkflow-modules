from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .network_manager_nat_rule import NetworkManagerNatRule


class NetworkManagerUpdateAttachmentNatConfigurationResponse(BaseModel):
    AttachmentId: StrictStr | None = None
    NatGatewaySupport: StrictStr | None = None
    NatSystemRouteSupport: StrictBool | None = None
    NatGatewayRules: list[NetworkManagerNatRule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
