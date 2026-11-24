from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTAuditCheckConfiguration(BaseModel):
    enabled: StrictBool | None = None
    configuration: dict[StrictStr, StrictStr] | None = None
