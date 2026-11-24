from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EKSCertificateAuthoritySummary(BaseModel):
    id: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    activatedAt: datetime.datetime | StrictStr | None = None
    activatedBy: StrictStr | None = None
    signingStatus: StrictStr | None = None
    distributionStatus: StrictStr | None = None
