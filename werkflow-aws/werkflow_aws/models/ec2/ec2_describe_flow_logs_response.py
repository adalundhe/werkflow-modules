from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_flow_log import EC2FlowLog


class EC2DescribeFlowLogsResponse(BaseModel):
    FlowLogs: list[EC2FlowLog] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
