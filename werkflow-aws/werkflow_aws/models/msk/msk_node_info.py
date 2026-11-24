from __future__ import annotations
from pydantic import BaseModel, StrictStr
from typing import Any


class MSKNodeInfo(BaseModel):
    AddedToClusterTime: StrictStr | None = None
    BrokerNodeInfo: dict[str, Any] | None = None
    ControllerNodeInfo: dict[str, Any] | None = None
    InstanceType: StrictStr | None = None
    NodeARN: StrictStr | None = None
    NodeType: StrictStr | None = None
    ZookeeperNodeInfo: dict[str, Any] | None = None
