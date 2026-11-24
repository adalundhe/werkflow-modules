from __future__ import annotations
from pydantic import BaseModel, StrictInt


class MacieBucketCountByEffectivePermission(BaseModel):
    publiclyAccessible: StrictInt | None = None
    publiclyReadable: StrictInt | None = None
    publiclyWritable: StrictInt | None = None
    unknown: StrictInt | None = None
