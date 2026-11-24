from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AWSS3RenameObjectRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    RenameSource: StrictStr
    DestinationIfMatch: StrictStr | None = None
    DestinationIfNoneMatch: StrictStr | None = None
    DestinationIfModifiedSince: datetime.datetime | StrictStr | None = None
    DestinationIfUnmodifiedSince: datetime.datetime | StrictStr | None = None
    SourceIfMatch: StrictStr | None = None
    SourceIfNoneMatch: StrictStr | None = None
    SourceIfModifiedSince: datetime.datetime | StrictStr | None = None
    SourceIfUnmodifiedSince: datetime.datetime | StrictStr | None = None
    ClientToken: StrictStr | None = None
