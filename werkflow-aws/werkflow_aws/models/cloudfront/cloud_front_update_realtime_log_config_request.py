from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_end_point import CloudFrontEndPoint


class CloudFrontUpdateRealtimeLogConfigRequest(BaseModel):
    EndPoints: list[CloudFrontEndPoint] | None = None
    Fields: list[StrictStr] | None = None
    Name: StrictStr | None = None
    ARN: StrictStr | None = None
    SamplingRate: StrictInt | None = None
