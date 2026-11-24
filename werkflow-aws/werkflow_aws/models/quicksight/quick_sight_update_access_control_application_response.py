from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightUpdateAccessControlApplicationResponse(BaseModel):
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ApplicationId: StrictStr | None = None
    Arn: StrictStr | None = None
    AccessControlApplicationStatus: StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
