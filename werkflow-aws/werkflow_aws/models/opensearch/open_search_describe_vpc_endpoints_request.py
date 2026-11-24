from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDescribeVpcEndpointsRequest(BaseModel):
    VpcEndpointIds: list[StrictStr]
