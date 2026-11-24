from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailBucketCorsRule(BaseModel):
    id: StrictStr | None = None
    allowedMethods: list[StrictStr] | None = None
    allowedOrigins: list[StrictStr] | None = None
    allowedHeaders: list[StrictStr] | None = None
    exposeHeaders: list[StrictStr] | None = None
    maxAgeSeconds: StrictInt | None = None
