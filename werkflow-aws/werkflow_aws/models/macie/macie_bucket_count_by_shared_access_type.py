from __future__ import annotations
from pydantic import BaseModel, StrictInt


class MacieBucketCountBySharedAccessType(BaseModel):
    external: StrictInt | None = None
    internal: StrictInt | None = None
    notShared: StrictInt | None = None
    unknown: StrictInt | None = None
