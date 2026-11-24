from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class QuickSightDescribeAutomationJobResponse(BaseModel):
    Arn: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    StartedAt: datetime.datetime | StrictStr | None = None
    EndedAt: datetime.datetime | StrictStr | None = None
    JobStatus: StrictStr | None = None
    InputPayload: StrictStr | None = None
    OutputPayload: StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
