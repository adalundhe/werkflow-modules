from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecs_gateway_cluster_association_summary import ECSGatewayClusterAssociationSummary


class ECSListGatewayClusterAssociationsResponse(BaseModel):
    gatewayClusterAssociations: list[ECSGatewayClusterAssociationSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
