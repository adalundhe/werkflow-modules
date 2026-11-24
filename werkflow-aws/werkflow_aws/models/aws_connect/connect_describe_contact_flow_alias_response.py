from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_contact_flow_alias_info import ConnectContactFlowAliasInfo


class ConnectDescribeContactFlowAliasResponse(BaseModel):
    ContactFlowAlias: ConnectContactFlowAliasInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
