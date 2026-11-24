from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTViolationEventAdditionalInfo(BaseModel):
    confidenceLevel: StrictStr | None = None
