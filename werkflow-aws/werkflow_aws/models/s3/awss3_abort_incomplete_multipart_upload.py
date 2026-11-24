from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AWSS3AbortIncompleteMultipartUpload(BaseModel):
    DaysAfterInitiation: StrictInt | None = None
