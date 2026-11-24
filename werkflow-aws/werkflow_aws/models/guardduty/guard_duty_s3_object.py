from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyS3Object(BaseModel):
    ETag: StrictStr | None = None
    Key: StrictStr | None = None
    VersionId: StrictStr | None = None
