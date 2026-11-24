from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieS3WordsList(BaseModel):
    bucketName: StrictStr | None = None
    objectKey: StrictStr | None = None
