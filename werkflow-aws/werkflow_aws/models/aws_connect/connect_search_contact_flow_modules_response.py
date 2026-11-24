from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_contact_flow_module import ConnectContactFlowModule


class ConnectSearchContactFlowModulesResponse(BaseModel):
    ContactFlowModules: list[ConnectContactFlowModule] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
