from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2GetPasswordDataResponse(BaseModel):
    InstanceId: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
    PasswordData: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
