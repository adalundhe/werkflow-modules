from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerDescribeImageResponse(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    FailureReason: StrictStr | None = None
    ImageArn: StrictStr | None = None
    ImageName: StrictStr | None = None
    ImageStatus: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    RoleArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
