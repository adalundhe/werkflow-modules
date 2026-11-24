from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SESSOARecord(BaseModel):
    PrimaryNameServer: StrictStr | None = None
    AdminEmail: StrictStr | None = None
    SerialNumber: StrictInt | None = None
