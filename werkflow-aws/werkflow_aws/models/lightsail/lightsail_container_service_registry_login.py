from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailContainerServiceRegistryLogin(BaseModel):
    username: StrictStr | None = None
    password: StrictStr | None = None
    expiresAt: datetime.datetime | StrictStr | None = None
    registry: StrictStr | None = None
