from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IoTLoggingOptionsPayload(BaseModel):
    roleArn: StrictStr
    logLevel: Literal['DEBUG', 'INFO', 'ERROR', 'WARN', 'DISABLED'] | None = None
