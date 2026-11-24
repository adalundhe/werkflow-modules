from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTHttpUrlDestinationProperties(BaseModel):
    confirmationUrl: StrictStr | None = None
