from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LightsailSetResourceAccessForBucketRequest(BaseModel):
    resourceName: StrictStr
    bucketName: StrictStr
    access: Literal['allow', 'deny']
