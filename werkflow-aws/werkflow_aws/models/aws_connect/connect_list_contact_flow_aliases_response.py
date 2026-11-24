from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_contact_flow_alias_summary import ConnectContactFlowAliasSummary


class ConnectListContactFlowAliasesResponse(BaseModel):
    ContactFlowAliasSummaryList: list[ConnectContactFlowAliasSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
