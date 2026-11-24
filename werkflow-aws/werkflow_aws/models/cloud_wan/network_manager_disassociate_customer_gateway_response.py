from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_customer_gateway_association import NetworkManagerCustomerGatewayAssociation


class NetworkManagerDisassociateCustomerGatewayResponse(BaseModel):
    CustomerGatewayAssociation: NetworkManagerCustomerGatewayAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
