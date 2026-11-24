from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailPartnerInfo(BaseModel):
    enrolledAt: datetime.datetime | StrictStr | None = None
    tierName: StrictStr | None = None
    status: StrictStr | None = None
