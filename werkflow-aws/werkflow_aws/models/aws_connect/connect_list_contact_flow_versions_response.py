from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_contact_flow_version_summary import ConnectContactFlowVersionSummary


class ConnectListContactFlowVersionsResponse(BaseModel):
    ContactFlowVersionSummaryList: list[ConnectContactFlowVersionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
