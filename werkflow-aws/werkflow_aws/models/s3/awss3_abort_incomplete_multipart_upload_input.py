from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AWSS3AbortIncompleteMultipartUploadInput(BaseModel):
    DaysAfterInitiation: StrictInt | None = None
