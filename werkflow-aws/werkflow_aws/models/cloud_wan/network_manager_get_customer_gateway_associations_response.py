from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_customer_gateway_association import NetworkManagerCustomerGatewayAssociation


class NetworkManagerGetCustomerGatewayAssociationsResponse(BaseModel):
    CustomerGatewayAssociations: list[NetworkManagerCustomerGatewayAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
