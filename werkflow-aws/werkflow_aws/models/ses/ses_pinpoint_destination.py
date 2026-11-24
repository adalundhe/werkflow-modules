from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESPinpointDestination(BaseModel):
    ApplicationArn: StrictStr | None = None
