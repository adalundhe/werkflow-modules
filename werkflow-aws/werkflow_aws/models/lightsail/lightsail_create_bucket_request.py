from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .lightsail_tag import LightsailTag


class LightsailCreateBucketRequest(BaseModel):
    bucketName: StrictStr
    bundleId: StrictStr
    tags: list[LightsailTag] | None = None
    enableObjectVersioning: StrictBool | None = None
