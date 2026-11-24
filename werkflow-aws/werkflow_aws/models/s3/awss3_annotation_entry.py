from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3AnnotationEntry(BaseModel):
    AnnotationName: StrictStr | None = None
    LastModified: datetime.datetime | StrictStr | None = None
    ETag: StrictStr | None = None
    ChecksumAlgorithm: list[StrictStr] | None = None
    Size: StrictInt | None = None
    ReplicationStatus: StrictStr | None = None
