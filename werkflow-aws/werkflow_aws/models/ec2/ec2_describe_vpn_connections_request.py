from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeVpnConnectionsRequest(BaseModel):
    Filters: list[EC2FilterModel] | None = None
    VpnConnectionIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
