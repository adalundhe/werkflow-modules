from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyUpdateS3BucketResource(BaseModel):
    ObjectPrefixes: list[StrictStr] | None = None
