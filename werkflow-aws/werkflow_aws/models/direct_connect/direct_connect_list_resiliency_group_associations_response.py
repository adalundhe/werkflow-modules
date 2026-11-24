from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_resiliency_group_association import DirectConnectResiliencyGroupAssociation


class DirectConnectListResiliencyGroupAssociationsResponse(BaseModel):
    items: list[DirectConnectResiliencyGroupAssociation] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
