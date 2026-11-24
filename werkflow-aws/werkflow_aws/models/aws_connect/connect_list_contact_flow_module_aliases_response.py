from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_contact_flow_module_alias_summary import ConnectContactFlowModuleAliasSummary


class ConnectListContactFlowModuleAliasesResponse(BaseModel):
    ContactFlowModuleAliasSummaryList: list[ConnectContactFlowModuleAliasSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
