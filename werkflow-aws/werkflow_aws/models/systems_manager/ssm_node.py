from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_node_owner_info import SSMNodeOwnerInfo
from .ssm_node_type import SSMNodeType


class SSMNode(BaseModel):
    CaptureTime: datetime.datetime | StrictStr | None = None
    Id: StrictStr | None = None
    Owner: SSMNodeOwnerInfo | None = None
    Region: StrictStr | None = None
    NodeType: SSMNodeType | None = None
