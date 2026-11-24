from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2StorageLocation(BaseModel):
    Bucket: StrictStr | None = None
    Key: StrictStr | None = None
