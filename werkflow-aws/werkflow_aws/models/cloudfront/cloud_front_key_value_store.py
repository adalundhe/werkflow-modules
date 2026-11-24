from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudFrontKeyValueStore(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Comment: StrictStr | None = None
    ARN: StrictStr | None = None
    Status: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
