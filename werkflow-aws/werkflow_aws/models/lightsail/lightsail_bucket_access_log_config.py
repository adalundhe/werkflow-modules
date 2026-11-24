from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailBucketAccessLogConfig(BaseModel):
    enabled: StrictBool | None = None
    destination: StrictStr | None = None
    prefix: StrictStr | None = None
