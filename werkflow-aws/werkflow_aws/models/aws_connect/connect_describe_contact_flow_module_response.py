from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_contact_flow_module import ConnectContactFlowModule


class ConnectDescribeContactFlowModuleResponse(BaseModel):
    ContactFlowModule: ConnectContactFlowModule | None = None
    ResponseMetadata: dict[str, Any] | None = None
