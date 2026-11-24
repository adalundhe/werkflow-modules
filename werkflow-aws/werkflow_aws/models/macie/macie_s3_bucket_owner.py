from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieS3BucketOwner(BaseModel):
    displayName: StrictStr | None = None
    id: StrictStr | None = None
