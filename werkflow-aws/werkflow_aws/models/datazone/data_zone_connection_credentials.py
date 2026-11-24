from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneConnectionCredentials(BaseModel):
    accessKeyId: StrictStr | None = None
    secretAccessKey: StrictStr | None = None
    sessionToken: StrictStr | None = None
    expiration: datetime.datetime | StrictStr | None = None
