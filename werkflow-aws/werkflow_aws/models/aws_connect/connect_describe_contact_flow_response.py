from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_contact_flow import ConnectContactFlow


class ConnectDescribeContactFlowResponse(BaseModel):
    ContactFlow: ConnectContactFlow | None = None
    ResponseMetadata: dict[str, Any] | None = None
