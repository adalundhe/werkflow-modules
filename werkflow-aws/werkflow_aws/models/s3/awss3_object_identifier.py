from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3ObjectIdentifier(BaseModel):
    Key: StrictStr
    VersionId: StrictStr | None = None
    ETag: StrictStr | None = None
    LastModifiedTime: datetime.datetime | str | None = None
    Size: StrictInt | None = None
