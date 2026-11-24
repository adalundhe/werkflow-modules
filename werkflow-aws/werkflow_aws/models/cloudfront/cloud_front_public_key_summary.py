from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudFrontPublicKeySummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    EncodedKey: StrictStr | None = None
    Comment: StrictStr | None = None
