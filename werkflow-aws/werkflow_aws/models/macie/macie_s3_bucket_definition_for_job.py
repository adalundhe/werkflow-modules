from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieS3BucketDefinitionForJob(BaseModel):
    accountId: StrictStr | None = None
    buckets: list[StrictStr] | None = None
