from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_operation_event import CloudFormationOperationEvent


class CloudFormationDescribeEventsResponse(BaseModel):
    OperationEvents: list[CloudFormationOperationEvent] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
