from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_contact_flow_module_summary import ConnectContactFlowModuleSummary


class ConnectListContactFlowModulesResponse(BaseModel):
    ContactFlowModulesSummaryList: list[ConnectContactFlowModuleSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
