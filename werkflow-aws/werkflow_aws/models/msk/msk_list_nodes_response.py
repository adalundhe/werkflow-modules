from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_node_info import MSKNodeInfo


class MSKListNodesResponse(BaseModel):
    NextToken: StrictStr | None = None
    NodeInfoList: list[MSKNodeInfo] | None = None
