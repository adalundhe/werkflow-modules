from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationDescribeStackDriftDetectionStatusResponse(BaseModel):
    StackId: StrictStr | None = None
    StackDriftDetectionId: StrictStr | None = None
    StackDriftStatus: StrictStr | None = None
    DetectionStatus: StrictStr | None = None
    DetectionStatusReason: StrictStr | None = None
    DriftedStackResourceCount: StrictInt | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
