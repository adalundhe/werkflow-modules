from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockS3Config(BaseModel):
    bucketName: StrictStr | None = None
    keyPrefix: StrictStr | None = None
