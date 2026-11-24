from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTHttpUrlDestinationSummary(BaseModel):
    confirmationUrl: StrictStr | None = None
