from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTGetLoggingOptionsResponse(BaseModel):
    roleArn: StrictStr | None = None
    logLevel: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
