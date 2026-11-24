from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueConnectionPasswordEncryption(BaseModel):
    ReturnConnectionPasswordEncrypted: StrictBool | None = None
    AwsKmsKeyId: StrictStr | None = None
