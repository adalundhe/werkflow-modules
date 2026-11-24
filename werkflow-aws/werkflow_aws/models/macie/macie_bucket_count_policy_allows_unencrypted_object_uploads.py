from __future__ import annotations
from pydantic import BaseModel, StrictInt


class MacieBucketCountPolicyAllowsUnencryptedObjectUploads(BaseModel):
    allowsUnencryptedObjectUploads: StrictInt | None = None
    deniesUnencryptedObjectUploads: StrictInt | None = None
    unknown: StrictInt | None = None
