from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MSKStartTopicReassignmentResponse(BaseModel):
    ClusterArn: StrictStr | None = None
    Status: StrictStr | None = None
    TopicReassignmentOperationArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
