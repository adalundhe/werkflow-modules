from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_contact_flow_module_version_summary import ConnectContactFlowModuleVersionSummary


class ConnectListContactFlowModuleVersionsResponse(BaseModel):
    ContactFlowModuleVersionSummaryList: list[ConnectContactFlowModuleVersionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
