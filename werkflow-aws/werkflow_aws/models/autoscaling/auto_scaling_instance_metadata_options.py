from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AutoScalingInstanceMetadataOptions(BaseModel):
    HttpTokens: StrictStr | None = None
    HttpPutResponseHopLimit: StrictInt | None = None
    HttpEndpoint: StrictStr | None = None
