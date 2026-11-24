from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_end_point import CloudFrontEndPoint


class CloudFrontRealtimeLogConfig(BaseModel):
    ARN: StrictStr | None = None
    Name: StrictStr | None = None
    SamplingRate: StrictInt | None = None
    EndPoints: list[CloudFrontEndPoint] | None = None
    Fields: list[StrictStr] | None = None
