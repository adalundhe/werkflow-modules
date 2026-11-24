from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt


class CloudFrontResponseHeadersPolicyServerTimingHeadersConfig(BaseModel):
    Enabled: StrictBool | None = None
    SamplingRate: StrictFloat | StrictInt | None = None
