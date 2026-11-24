from __future__ import annotations
from pydantic import BaseModel, StrictBool


class IoTGetV2LoggingOptionsRequest(BaseModel):
    verbose: StrictBool | None = None
