from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_contact_flow_summary import ConnectContactFlowSummary


class ConnectListContactFlowsResponse(BaseModel):
    ContactFlowSummaryList: list[ConnectContactFlowSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
