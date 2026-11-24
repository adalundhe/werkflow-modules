from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDnsRecordCreationState(BaseModel):
    code: StrictStr | None = None
    message: StrictStr | None = None
