from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_registered_instance import EC2RegisteredInstance


class EC2DescribeInstanceSqlHaHistoryStatesResponse(BaseModel):
    Instances: list[EC2RegisteredInstance] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
