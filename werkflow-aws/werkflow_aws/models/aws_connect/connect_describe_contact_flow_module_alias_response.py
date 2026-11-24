from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_contact_flow_module_alias_info import ConnectContactFlowModuleAliasInfo


class ConnectDescribeContactFlowModuleAliasResponse(BaseModel):
    ContactFlowModuleAlias: ConnectContactFlowModuleAliasInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
