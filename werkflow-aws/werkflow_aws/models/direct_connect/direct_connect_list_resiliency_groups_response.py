from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_resiliency_group_summary import DirectConnectResiliencyGroupSummary


class DirectConnectListResiliencyGroupsResponse(BaseModel):
    items: list[DirectConnectResiliencyGroupSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
