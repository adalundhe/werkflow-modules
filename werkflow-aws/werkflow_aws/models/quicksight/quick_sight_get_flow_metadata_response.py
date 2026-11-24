from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightGetFlowMetadataResponse(BaseModel):
    Arn: StrictStr | None = None
    FlowId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    PublishState: StrictStr | None = None
    UserCount: StrictInt | None = None
    RunCount: StrictInt | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
