from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EKSCertificateAuthorityScheduledEvents(BaseModel):
    firstAutoActivation: datetime.datetime | StrictStr | None = None
    finalAutoActivation: datetime.datetime | StrictStr | None = None
