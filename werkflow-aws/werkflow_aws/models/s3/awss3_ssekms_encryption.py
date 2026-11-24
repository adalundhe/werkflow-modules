from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AWSS3SSEKMSEncryption(BaseModel):
    KMSKeyArn: StrictStr
    BucketKeyEnabled: StrictBool | None = None
