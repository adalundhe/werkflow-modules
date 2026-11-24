from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTHttpUrlDestinationConfiguration(BaseModel):
    confirmationUrl: StrictStr
