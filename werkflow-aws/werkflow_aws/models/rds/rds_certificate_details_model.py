from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class RDSCertificateDetailsModel(BaseModel):
    CAIdentifier: StrictStr | None = None
    ValidTill: datetime.datetime | StrictStr | None = None
