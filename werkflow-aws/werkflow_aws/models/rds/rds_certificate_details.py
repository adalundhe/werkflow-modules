from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class RDSCertificateDetails(BaseModel):
    CAIdentifier: StrictStr | None = None
    ValidTill: datetime.datetime | None = None
