from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeS3Location(BaseModel):
    uri: StrictStr | None = None
    bucketOwner: StrictStr | None = None
