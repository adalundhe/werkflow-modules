from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_node import SSMNode


class SSMListNodesResponse(BaseModel):
    Nodes: list[SSMNode] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
