from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2GetConsoleOutputResponse(BaseModel):
    InstanceId: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
    Output: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
