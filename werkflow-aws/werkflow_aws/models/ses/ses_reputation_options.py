from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class SESReputationOptions(BaseModel):
    ReputationMetricsEnabled: StrictBool | None = None
    LastFreshStart: datetime.datetime | StrictStr | None = None
