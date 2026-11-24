from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class MediaStoreContainer(BaseModel):
    Endpoint: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ARN: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    AccessLoggingEnabled: StrictBool | None = None
