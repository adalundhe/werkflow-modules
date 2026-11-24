from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyCreateS3BucketResource(BaseModel):
    BucketName: StrictStr | None = None
    ObjectPrefixes: list[StrictStr] | None = None
