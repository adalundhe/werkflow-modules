from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyS3ObjectDetail(BaseModel):
    ObjectArn: StrictStr | None = None
    Key: StrictStr | None = None
    ETag: StrictStr | None = None
    Hash: StrictStr | None = None
    VersionId: StrictStr | None = None
