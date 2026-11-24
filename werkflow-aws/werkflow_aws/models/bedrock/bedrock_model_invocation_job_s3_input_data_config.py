from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockModelInvocationJobS3InputDataConfig(BaseModel):
    s3InputFormat: StrictStr | None = None
    s3Uri: StrictStr | None = None
    s3BucketOwner: StrictStr | None = None
