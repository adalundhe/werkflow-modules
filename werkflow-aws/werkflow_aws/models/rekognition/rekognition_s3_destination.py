from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionS3Destination(BaseModel):
    Bucket: StrictStr | None = None
    KeyPrefix: StrictStr | None = None
