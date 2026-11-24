from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailAccountLevelBpaSync(BaseModel):
    status: StrictStr | None = None
    lastSyncedAt: datetime.datetime | StrictStr | None = None
    message: StrictStr | None = None
    bpaImpactsLightsail: StrictBool | None = None
