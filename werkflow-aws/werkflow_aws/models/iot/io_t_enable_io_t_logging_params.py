from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTEnableIoTLoggingParams(BaseModel):
    roleArnForLogging: StrictStr | None = None
    logLevel: StrictStr | None = None
