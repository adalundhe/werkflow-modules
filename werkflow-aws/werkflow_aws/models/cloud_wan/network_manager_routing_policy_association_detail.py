from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerRoutingPolicyAssociationDetail(BaseModel):
    RoutingPolicyNames: list[StrictStr] | None = None
    SharedSegments: list[StrictStr] | None = None
