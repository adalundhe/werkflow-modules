from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class EC2S3Storage(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    AWSAccessKeyId: StrictStr | None = None
    Bucket: StrictStr | None = None
    Prefix: StrictStr | None = None
    UploadPolicy: StrictBytes | Any | None = None
    UploadPolicySignature: StrictStr | None = None
