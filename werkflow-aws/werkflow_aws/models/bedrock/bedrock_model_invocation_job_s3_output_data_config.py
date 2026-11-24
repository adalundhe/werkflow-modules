from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockModelInvocationJobS3OutputDataConfig(BaseModel):
    s3Uri: StrictStr | None = None
    s3EncryptionKeyId: StrictStr | None = None
    s3BucketOwner: StrictStr | None = None
