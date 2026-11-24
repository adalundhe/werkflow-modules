from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AWSS3AbortIncompleteMultipartUploadModel(BaseModel):
    DaysAfterInitiation: StrictInt | None = None
