from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_stack_event import CloudFormationStackEvent


class CloudFormationDescribeStackEventsResponse(BaseModel):
    StackEvents: list[CloudFormationStackEvent] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
