from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTLogEventConfiguration(BaseModel):
    eventType: StrictStr | None = None
    logLevel: StrictStr | None = None
    logDestination: StrictStr | None = None
