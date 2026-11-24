from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class XRaySamplingBoost(BaseModel):
    BoostRate: StrictFloat | StrictInt | None = None
    BoostRateTTL: datetime.datetime | StrictStr | None = None
