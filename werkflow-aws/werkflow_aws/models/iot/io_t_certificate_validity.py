from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTCertificateValidity(BaseModel):
    notBefore: datetime.datetime | StrictStr | None = None
    notAfter: datetime.datetime | StrictStr | None = None
