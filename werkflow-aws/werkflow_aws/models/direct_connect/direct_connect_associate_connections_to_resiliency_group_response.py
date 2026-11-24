from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .direct_connect_resiliency_group_association import DirectConnectResiliencyGroupAssociation


class DirectConnectAssociateConnectionsToResiliencyGroupResponse(BaseModel):
    resiliencyGroupAssociations: list[DirectConnectResiliencyGroupAssociation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
