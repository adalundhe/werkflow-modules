from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3NoncurrentVersionTransitionModel(BaseModel):
    NoncurrentDays: StrictInt | None = None
    StorageClass: StrictStr | None = None
    NewerNoncurrentVersions: StrictInt | None = None
