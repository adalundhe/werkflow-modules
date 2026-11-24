from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSS3GetObjectTorrentRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    RequestPayer: Literal['requester'] | None = None
    ExpectedBucketOwner: StrictStr | None = None
