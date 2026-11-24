from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDestination(BaseModel):
    ToAddresses: list[StrictStr] | None = None
    CcAddresses: list[StrictStr] | None = None
    BccAddresses: list[StrictStr] | None = None
