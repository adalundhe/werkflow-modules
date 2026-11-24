from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class DataZoneGetEnvironmentCredentialsResponse(BaseModel):
    accessKeyId: StrictStr | None = None
    secretAccessKey: StrictStr | None = None
    sessionToken: StrictStr | None = None
    expiration: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
