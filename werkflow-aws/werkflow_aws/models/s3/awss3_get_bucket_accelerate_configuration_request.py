from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3GetBucketAccelerateConfigurationRequest(BaseModel):
    Bucket: StrictStr
    ExpectedBucketOwner: StrictStr | None = None
    RequestPayer: Literal['requester'] | None = None
