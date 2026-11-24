from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeAsyncInvokeS3OutputDataConfig(BaseModel):
    s3Uri: StrictStr | None = None
    kmsKeyId: StrictStr | None = None
    bucketOwner: StrictStr | None = None
